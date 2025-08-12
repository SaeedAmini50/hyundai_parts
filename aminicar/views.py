from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AccountAuthenticationForm , RegistrationForm,AccountUpdateForm
from django.contrib.auth import authenticate, login ,logout
from aminicar.models import Account
from django.conf import settings
from django.contrib import messages 
from django.shortcuts import get_object_or_404




def not_find(request, exception):
    return render(request, 'aminicar/form/404.html', status=404)



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

    # بررسی اینکه آیا کاربر قبلاً وارد شده است
    if user.is_authenticated:
        messages.info(request, 'You are already signed in to your account.')
        return redirect('aminicar:index')

    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')

            # احراز هویت کاربر
            user = authenticate(email=email, password=raw_password)
            if user:
                login(request, user)
                messages.success(request, 'Welcome! You have signed in successfully.')
                return redirect('aminicar:index')
            else:
                messages.error(request, 'Incorrect email or password. Please try again.')
        else:
            messages.error(request, 'Please complete the form correctly.')
    else:
        form = AccountAuthenticationForm()
        # نمایش پیام راهنما برای تکمیل فرم
        messages.info(request, 'Please enter your information.')

    context['login_form'] = form
    return render(request, 'aminicar/form/signin.html', context)
 
def register_signup(request, *args, **kwargs):
    user = request.user

    # بررسی اینکه آیا کاربر قبلاً وارد شده است
    if user.is_authenticated:
        messages.info(request, f'You are already signed in with the email address {user.email}.')
        return redirect("product:products")

    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')

            # احراز هویت و ورود به حساب کاربری
            account = authenticate(email=email, password=raw_password)
            if account:
                login(request, account)
                messages.success(request, 'You have successfully registered. Welcome!')
                destination = kwargs.get("next")
                if destination:
                    return redirect(destination)
                return redirect("product:products")
        else:
            # نمایش پیام خطاهای فرم
            context['registration_form'] = form
            error_messages = form.errors.as_text()
            print(error_messages)
            messages.error(request, 'Registration failed. Password must be over 8 characters, include uppercase and lowercase letters, symbols, and not resemble a Gmail address.')

    else:
        form = RegistrationForm()
        context['registration_form'] = form
        # پیام راهنما برای کاربران جدید
        messages.info(request, 'Please fill out the registration form carefully.')



    return render(request, 'aminicar/form/signup.html', context)
def logout_view(request):
    logout(request)
    return redirect('product:products')




def edit_account_view(request, *args, **kwargs):
    # بررسی احراز هویت کاربر
    if not request.user.is_authenticated:
        messages.warning(request, 'Please sign in to your account first.')
        return redirect('aminicar:signin')

    # دریافت اطلاعات حساب کاربری
    user_id = kwargs.get('user_id')
    account = get_object_or_404(Account, pk=user_id)

    # بررسی مالکیت پروفایل
    if account.pk != request.user.pk:
        messages.error(request, 'You do not have permission to edit this profile.')
        return HttpResponse("You are not allowed to edit this profile.")

    context = {}

    if request.method == "POST":
        form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been successfully updated.')
            return redirect('aminicar:profile', user_id=account.pk)
        else:
            messages.error(request, 'Please check the information you entered.')
    else:
        form = AccountUpdateForm(
            initial={
                'id': account.id,
                'email': account.email,
                'username': account.username,
                'profile_image': account.profile_image
            }
        )
    
    context['form'] = form
    context['user'] = account
    context['DATA_UPLOAD_MAX_MEMORY_SIZE'] = settings.DATA_UPLOAD_MAX_MEMORY_SIZE

    return render(request, 'aminicar/main/profile.html', context)