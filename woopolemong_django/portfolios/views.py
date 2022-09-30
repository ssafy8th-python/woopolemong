from django.shortcuts import render

# Create your views here.


def detail(request) :
    pass
    return render(request, 'portfolios/detail.html',)

def index(request) :
    return render(request, 'portfolios/index.html',)

def create(request) :
    return render(request, 'portfolios/create.html',)

def delete(request) :
    pass

def update(request) :
    return render(request, 'portfolios/update.html',)
