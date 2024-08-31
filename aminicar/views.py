from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AccountAuthenticationForm
from django.contrib.auth import authenticate, login
from aminicar.models import Account
from django.conf import settings
 


def index (requset):
    return render(requset,'aminicar/main/index.html', {'name':'saeedamini'})

def show_product (requset):
    return render(requset,'aminicar/main/show_product.html')

 
def signup (requset):
    return render(requset,'aminicar/form/signup.html')


 
def base(requset):
    return render(requset, 'aminicar/main/base.html')

def index(requset):
    return render(requset, 'aminicar/main/index.html')
 

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('aminicar:index')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            print(form,form.cleaned_data)
            print('form', form.cleaned_data)
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=raw_password)

        
            if user:
                login(request, user)
                return redirect('aminicar:index')
        else:
            print(form.errors) 
    else:
        form = AccountAuthenticationForm()
    
    context['login_form'] = form

    return render(request, 'aminicar/form/signin.html', context)

