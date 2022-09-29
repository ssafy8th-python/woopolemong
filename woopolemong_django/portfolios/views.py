from django.shortcuts import render

# Create your views here.


def detail(request) :
    pass
    return render(request, 'portfolios/detail.html',)

def index(request) :
    return render(request, 'portfolios/index.html',)

def create(request) :
    pass

def delete(request) :
    pass

def update(request) :
    pass
