from django.shortcuts import render, redirect
from .models import Product ,Cart
from django.http import JsonResponse
import json
from django.contrib import messages 
from django.shortcuts import get_object_or_404



def view_product(request):
    context = {}
    products = Product.objects.all()
    context['products'] = products
    return render(request, 'aminicar/main/index.html', context)



 
def product_detail(request, product_id):
    context = {}
    product = Product.objects.get(id=product_id)

    context['product'] = product

    return render(request, 'aminicar/main/show_product.html', context)

def add_to_cart(request):
    current_user = request.user
    if request.method == "POST":
        if request.user.is_authenticated:
            product_id = int(request.POST.get('product_id'))
            print('Product ID:', product_id)
            # منطق اضافه کردن محصول به سبد خرید

            try:
                product_check = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                messages.error(request, 'محصولی با این شناسه یافت نشد. لطفاً دوباره تلاش کنید.')
                return JsonResponse({'status': 'No such Product found'})

            if product_check:
                if Cart.objects.filter(user=current_user, product_id=product_id):
                    messages.warning(request, 'این محصول قبلاً به سبد خرید شما اضافه شده است.')
                    return JsonResponse({'status': 'Product is Already in Cart'})
                else:
                    product_qyt = 1
                    Cart.objects.create(user=current_user, product_id=product_id, quantity=product_qyt)
                    messages.success(request, 'محصول با موفقیت به سبد خرید شما اضافه شد.')
                    return JsonResponse({'status': 'Product added successfully'})

        else:
            messages.error(request, 'لطفاً ابتدا وارد حساب کاربری خود شوید.')
            return JsonResponse({'status': 'Login to continue'})

    messages.error(request, 'درخواست نادرست است. لطفاً دوباره تلاش کنید.')
    return JsonResponse({'status': 'Invalid request'}, status=400)




def checkout(request):
    if not request.user.is_authenticated:
        messages.error(request, 'لطفاً ابتدا وارد حساب کاربری خود شوید.')
        return redirect('login')  # یا صفحه‌ای که کاربر را به ورود هدایت کند

    context = {}
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items.exists():
        messages.warning(request, 'سبد خرید شما خالی است. لطفاً محصولی به سبد خرید اضافه کنید.')
        return redirect('cart')  # یا هر صفحه‌ای که محصولات را نمایش می‌دهد

    context['cart_items'] = cart_items
    context['cart_total'] = cart_items.count()

    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.quantity  # جمع کل قیمت محصولات با تعداد

    context['total_price'] = total_price


    messages.info(request, 'لطفاً جزئیات پرداخت خود را بررسی کنید.')

    return render(request, 'aminicar/main/checkout.html', context)
