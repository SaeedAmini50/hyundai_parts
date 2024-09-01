from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AccountAuthenticationForm , RegistrationForm
from django.contrib.auth import authenticate, login ,logout
from aminicar.models import Account
from django.conf import settings
 

def indexAdmin (requset):
    return render(requset,'aminicar/dashboard/indexAdmin.html')




def index (requset):
    return render(requset,'aminicar/main/index.html', {'name':'saeedamini'})


def base (requset):
    return render(requset,'aminicar/main/index_base.html')

def show_product (requset):
    return render(requset,'aminicar/main/show_product.html')

 
def signup (requset):
    return render(requset,'aminicar/form/signup.html')


 
def index(requset):
    return render(requset, 'aminicar/main/index.html')
 

def register_signin(request):
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



def register_signup(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.email))

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect("aminicar:index")
        else:
            context['registration_form'] = form
            print(form.errors) 

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'aminicar/form/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('aminicar:index')



