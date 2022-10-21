from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Portfolio
from .forms import PortfolioForm, Portfolio_imageForm
# Create your views here.


@require_safe
def index(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios': portfolios,
    }
    return render(request, 'portfolios/index.html', context)


@require_safe
def detail(request, portfolio_pk):
    portfolio = Portfolio.objects.get(pk=portfolio_pk)
    images = portfolio.portfolio_image_set.all()
    context = {
        'portfolio': portfolio,
        'images': images,
    }
    return render(request, 'portfolios/detail.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # 게시글
            form = PortfolioForm(request.POST)
            image_form = Portfolio_imageForm(request.POST, request.FILES)
            if form.is_valid() and image_form.is_valid():
                portfolio = form.save(commit=False)
                portfolio.author = request.user
                portfolio.save()
                # 이미지
                image = image_form.save(commit=False)
                image.portfolio = portfolio
                image.save()
                return redirect('portfolios:detail', portfolio.pk)
        else:
            form = PortfolioForm()
            image_form = Portfolio_imageForm()
        context = {
            'form': form,
            'image_form': image_form
        }
        return render(request, 'portfolios/create.html', context)
    else:
        return redirect('portfolios:index')


@require_http_methods(['GET', 'POST'])
def update(request, portfolio_pk):
    portfolio = Portfolio.objects.get(pk=portfolio_pk)
    if request.user == portfolio.author:
        if request.method == 'POST':
            form = PortfolioForm(request.POST, instance=portfolio)
            image_form = Portfolio_imageForm(request.POST, request.FILES, instance=portfolio.portfolio_image_set.all())
            if form.is_valid() and image_form.is_valid():
                form.save()
                image_form.save()
                return redirect('portfolios:detail', portfolio.pk)
        else:
            form = PortfolioForm(instance=portfolio)
            image_form = Portfolio_imageForm(instance=portfolio.portfolio_image_set.all())
        context = {
                'form': form,
            }
        return render(request, 'portfolios/update.html', context)
    else:
        return redirect('portfolios:index')


@require_POST
def delete(request, portfolio_pk):
    portfolio = Portfolio.objects.get(pk=portfolio_pk)
    if request.user == portfolio.author:
        if request.method == 'POST':
            portfolio.delete()
            return redirect('portfolios:index')
    else:
        return redirect('portfolios:detail', portfolio.pk)

def projectlist(request) :
    projects = Portfolio.objects.order_by('-pk')
    context = {
        'projects' : projects,
    }
    return render(request, 'portfolios/projectlist.html', context)
