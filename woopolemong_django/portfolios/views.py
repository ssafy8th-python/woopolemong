from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Portfolio, Portfolio_image
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
            if form.is_valid():
                portfolio = form.save(commit=False)
                portfolio.author = request.user
                portfolio.save()

            # 이미지
            for photo in request.FILES.getlist('image'):
                request.FILES['image'] = photo
                image_form = Portfolio_imageForm(request.POST, request.FILES)
                if image_form.is_valid():
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
        return redirect('portfolios:projectlist')


@require_http_methods(['GET', 'POST'])
def update(request, portfolio_pk):
    portfolio = Portfolio.objects.get(pk=portfolio_pk)
    if request.user == portfolio.author:
        if request.method == 'POST':
            # 게시글
            form = PortfolioForm(request.POST, instance=portfolio)
            if form.is_valid():
                form.save()
            # 이미지
            for photo in request.FILES.getlist('image'):
                request.FILES['image'] = photo
                image_form = Portfolio_imageForm(request.POST, request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.portfolio = portfolio
                    image.save()
            return redirect('portfolios:detail', portfolio.pk)
        else:
            form = PortfolioForm(instance=portfolio)
            image_form = Portfolio_imageForm()
            db_images = portfolio.portfolio_image_set.all()
            
        context = {
                'form': form,
                'image_form': image_form,
                'db_images': db_images,
                'portfolio': portfolio,
            }
        return render(request, 'portfolios/update.html', context)
    else:
        return redirect('portfolios:detail', portfolio.pk)


@require_POST
def delete(request, portfolio_pk):
    portfolio = Portfolio.objects.get(pk=portfolio_pk)
    if request.user == portfolio.author:
        if request.method == 'POST':
            portfolio.delete()
            return redirect('portfolios:projectlist')
    else:
        return redirect('portfolios:detail', portfolio.pk)


def projectlist(request) :
    projects = Portfolio.objects.order_by('-pk')
    context = {
        'projects' : projects,
    }
    return render(request, 'portfolios/projectlist.html', context)


@require_POST
def image_delete(request, image_pk):
    if request.method == 'POST':
        image = Portfolio_image.objects.get(pk=image_pk)
        image.delete()
        data = {
            'header': 'sadf'
        }
        return JsonResponse(data)