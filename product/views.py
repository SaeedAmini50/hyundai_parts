from django.shortcuts import render, redirect
from .models import Product
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

