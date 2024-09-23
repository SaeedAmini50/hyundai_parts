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
    if request.method == "POST":
        if request.user.is_authenticated:
            product_id = int(request.POST.get('product_id'))
            print('hello saeedamini   product_id', product_id)
            # منطق اضافه کردن محصول به سبد خرید
            return JsonResponse({'status': "Product added successfully!"})
        else:
            return JsonResponse({'status': "login to continue"})
    return JsonResponse({'status': "Invalid request"}, status=400)
