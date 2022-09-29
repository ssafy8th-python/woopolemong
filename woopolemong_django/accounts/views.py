from django.shortcuts import render

# Create your views here.

def login(request):
    print('test')
    return render(request, 'accounts/login.html')

def logout():
    pass

def signup():
    pass

def signout():
    pass

def findpassword():
    pass
