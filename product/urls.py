from django.urls import path
from .views import view_product, product_detail,add_to_cart

app_name = 'product'

urlpatterns = [
    path('', view_product, name='products'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
    path('add_to_cart/',add_to_cart, name='add_to_cart'),

]
 


 