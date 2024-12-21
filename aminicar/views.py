from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AccountAuthenticationForm , RegistrationForm,AccountUpdateForm
from django.contrib.auth import authenticate, login ,logout
from aminicar.models import Account
from django.conf import settings
from django.contrib import messages 





def indexAdmin (requset):
    return render(requset,'aminicar/dashboard/indexAdmin.html')




def H2630035505 (requset):
    return render(requset,'aminicar/product/2630035505/2630035505.html')


def H319102H000 (requset):
    return render(requset,'aminicar/product/319102H000/319102H000.html')

def H2351025250 (requset):
    return render(requset,'aminicar/product/2351025250/2351025250.html')

def H311121R000 (requset):
    return render(requset,'aminicar/product/311121R000/311121R000.html')

def H273012B010 (requset):
    return render(requset,'aminicar/product/273012B010/273012B010.html')

def  H3C10028164 (requset):
    return render(requset,'aminicar/product/3C10028164/3C10028164.html')




def errorpage (requset):
    return render(requset,'aminicar/form/errorpage.html')


def not_find (requset):
    return render(requset,'aminicar/form/404.html')





def index (requset):
    return render(requset,'aminicar/main/index.html', {'name':'saeedamini'})





def base (requset):
    
    return render(requset,'aminicar/main/index_base.html')

def show_product(request):
    # ارسال پیام موفقیت به درخواست
    
    
    # رندر کردن صفحه HTML
    return render(request, 'aminicar/main/show_product.html')



 
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
                 messages.success(request, 'welcame')
                 return redirect('aminicar:index')
        else:
            messages.error(request, 'excuse me') 
    else:
        form = AccountAuthenticationForm()
        messages.error(request, 'complete')
    
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
            print(form.errors.as_text())


    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'aminicar/form/signup.html', context)

def logout_view(request):
    logout(request)
    return redirect('aminicar:index')




def edit_account_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('aminicar:signin')
    user_id = kwargs.get('user_id')
    account = Account.objects.get(pk=user_id)

    dic = {}

    if account.pk != request.user.pk:
        return HttpResponse("You cannot edit this profile")
    if request.POST:
        form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('aminicar:profile', user_id=account.pk)
        else:
            form = AccountUpdateForm(request.POST, instance=request.user,
            initial = {
                'id' : account.id,
                'email' : account.email,
                'username' : account.username,
                'profile_image' : account.profile_image
            }
            )
            dic['form'] = form

    else:
        form = AccountUpdateForm(
            initial = {
            'id' : account.id,
            'email' : account.email,
            'username' : account.username,
            'profile_image' : account.profile_image
            }
        )
        dic['form'] = form
        dic['user'] = account

    dic['DATA_UPLOAD_MAX_MEMORY_SIZE'] = settings.DATA_UPLOAD_MAX_MEMORY_SIZE
    return render(request, 'aminicar/main/profile.html', dic)

