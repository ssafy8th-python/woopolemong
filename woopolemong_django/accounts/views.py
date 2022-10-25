from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth import get_user_model
from accounts.forms import CustomUserCreationForm
import random


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('portfolios:index')

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


@require_POST
def logout(request):

    if request.user.is_authenticated:
        auth_logout(request)
    
    return redirect('portfolios:index')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('portfolios:index')

    pictures = ['cyk', 'jwj', 'khh', 'kty', 'sjw', 'ydh']
    picture = 'accounts/img/' + random.choice(pictures) + '.png'

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)

            return redirect('portfolios:index')

    elif request.method == 'GET':

        form = CustomUserCreationForm()

    context = {
        'form' : form,
        'picture' : picture,
    }

    return render(request, 'accounts/signup.html', context)


@require_POST
def signout(request):
    
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)

    return redirect('portfolios:index')


def findpassword():
    pass


@require_GET
def management(request, page):
    if request.user.is_superuser:
        User = get_user_model()
        users = User.objects.all()
        users = users[(page - 1) * 10:page*10 + 1]
        user_cnt = User.objects.count()

        if user_cnt % 10  :
            last_page = user_cnt // 10 + 1
        else:
            last_page = user_cnt // 10

        user_pages = [i for i in range(1, last_page+1)]

        context = {
            'users' : users,
            'user_pages' : user_pages,
            'cur_page' : page,
            'last_page' : last_page,
        }

        return render(request, 'accounts/management.html', context)
    else:
        return redirect('portfolios:index')


@require_http_methods(['POST'])
def change_authority(request, user_pk, cur_page):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)

    if request.user.is_superuser:

        if request.POST['authority'] == "2":
            user.is_superuser = 1
            user.is_staff = 1
            user.is_active = 1
        elif request.POST['authority'] == "1":
            user.is_superuser = 0
            user.is_staff = 1
            user.is_active = 1
        else:
            user.is_superuser = 0
            user.is_staff = 0
            user.is_active = 1
        
        user.save()
    else:
        return redirect('portfolios:index')

    return redirect('accounts:management', cur_page)