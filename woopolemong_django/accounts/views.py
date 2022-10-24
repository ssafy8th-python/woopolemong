from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from accounts.forms import CustomUserCreationForm
import random

def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('portfolios:index')
    elif request.method == 'GET':
        form = AuthenticationForm()
    
    context = {
        'form' : form,
    }

    return render(request, 'accounts/login.html', context)


def logout(request):

    if request.user.is_authenticated:
        auth_logout(request)
    
    return redirect('portfolios:index')


def signup(request):

    pictures = ['cyk', 'jwj', 'khh', 'kty', 'sjw', 'ydh']
    picture = 'accounts/img/' + random.choice(pictures) + '.png'

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolios:index')
    elif request.method == 'GET':

        form = CustomUserCreationForm()

    context = {
        'form' : form,
        'picture' : picture,
    }

    return render(request, 'accounts/signup.html', context)


def signout(request):
    
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)

    return redirect('portfolios:index')


def findpassword():
    pass
