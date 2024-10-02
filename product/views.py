from django.shortcuts import render, redirect
from .models import Product ,Cart
from django.http import JsonResponse
import json
 
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
    current_user=request.user
    if request.method == "POST":
        if request.user.is_authenticated:
            product_id = int(request.POST.get('product_id'))
            print('Product ID:', product_id)
            # منطق اضافه کردن محصول به سبد خرید

            product_check = Product.objects.get(id=product_id)
            if product_check:
                if Cart.objects.filter(user=current_user, product_id=product_id):
                    return JsonResponse({'status': 'Product is Already in Cart'})
                else:
                    product_qyt = 1
                    Cart.objects.create(user=current_user, product_id=product_id, quantity=product_qyt)
                    return JsonResponse({'status': 'Product added successfuly'})
            else:
                return JsonResponse({'status': 'No such Product found'})

        else:
            return JsonResponse({'status': "Login to continue"})
    return JsonResponse({'status': "Invalid request"}, status=400)
    return redirect('/')
  


def checkout(request):
    context = {}
    cart_items = Cart.objects.filter(user=request.user)

    context['cart_items'] = cart_items
    context['cart_total'] = cart_items.count()

    cart_total = 0
    total_price = 0
    if cart_items:
        for item in cart_items:
            total_price += item.product.price
            

        context['total_price'] = total_price
        
    
    return render(request, 'aminicar/main/checkout.html', context)
