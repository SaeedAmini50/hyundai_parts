from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AccountAuthenticationForm , RegistrationForm,AccountUpdateForm
from django.contrib.auth import authenticate, login ,logout
from aminicar.models import Account
from django.conf import settings
from django.contrib import messages 





def indexAdmin (requset):
    return render(requset,'aminicar/dashboard/indexAdmin.html')


def H213103E100 (requset):
    return render(requset,'aminicar/product/213103E100/213103E100.html')
def H230402G510 (requset):
    return render(requset,'aminicar/product/230402G510/230402G510.html')
def H231243C101 (requset):
    return render(requset,'aminicar/product/231243C101/231243C101.html')
def H231243C201 (requset):
    return render(requset,'aminicar/product/231243C201/231243C201.html')
def H231243E020 (requset):
    return render(requset,'aminicar/product/231243E020/231243E020.html')

def H234102G500 (requset):
    return render(requset,'aminicar/product/234102G500/234102G500.html')

def H234102G510 (requset):
    return render(requset,'aminicar/product/234102G510/234102G510.html')

def H263203C250 (requset):
    return render(requset,'aminicar/product/263203C250/263203C250.html')

def H273012B010 (requset):
    return render(requset,'aminicar/product/273012B010/273012B010.html')

def H517123L000 (requset):
    return render(requset,'aminicar/product/517123L000/517123L000.html')

def H584113L000 (requset):
    return render(requset,'aminicar/product/584113L000/584113L000.html')


def H1884111051 (requset):
    return render(requset,'aminicar/product/1884111051/1884111051.html')

def H230402B050 (requset):
    return render(requset,'aminicar/product/230402B050/230402B050.html')


def H1884511160 (requset):
    return render(requset,'aminicar/product/1884511160/1884511160.html')


def H1884511160_1 (requset):
    return render(requset,'aminicar/product/1884511160_1/1884511160_1.html')


def H1884911070 (requset):
    return render(requset,'aminicar/product/1884911070/1884911070.html')

def H2231125212 (requset):
    return render(requset,'aminicar/product/2231125212/2231125212.html')

def H2351025250 (requset):
    return render(requset,'aminicar/product/2351025250/2351025250.html')

def H2741023700 (requset):
    return render(requset,'aminicar/product/2741023700/2741023700.html')


def H5172038110 (requset):
    return render(requset,'aminicar/product/5172038110/5172038110.html')


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
    messages.success(request, 'خوش آمدید!')
    
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
            print(form.errors) 

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

