from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Portfolio
from .forms import PortfolioForm
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
    context = {
        'portfolio': portfolio,
    }
    return render(request, 'portfolios/detail.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PortfolioForm(request.POST)
            portfolio = form.save(commit=False)
            portfolio.author = request.user
            portfolio.save()
            return redirect('portfolios:detail', portfolio.pk)
        else:
            form = PortfolioForm()
        context = {
            'form': form,
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
            if form.is_valid:
                form.save()
                return redirect('portfolios:detail', portfolio.pk)
        else:
            form = PortfolioForm(instance=portfolio)
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
