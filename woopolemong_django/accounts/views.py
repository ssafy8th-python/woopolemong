from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('portfolios:index')
    elif request.method == 'GET':
        form = AuthenticationForm()
    
    context = {
        'form' : form
    }

    return render(request, 'accounts/login.html', context)


def logout():
    pass

def signup():
    pass

def signout():
    pass

def findpassword():
    pass
