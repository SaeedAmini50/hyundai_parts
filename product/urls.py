from django.urls import path
from .views import view_product, product_detail

app_name = 'product'

urlpatterns = [
    path('', view_product, name='products'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),

]
 