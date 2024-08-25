from django.shortcuts import render
from django.http import HttpResponse


def index (requset):
    return render(requset,'aminicar/main/index.html')

def show_product (requset):
    return render(requset,'aminicar/main/show_product.html')