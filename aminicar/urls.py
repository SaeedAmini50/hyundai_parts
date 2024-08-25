from django.urls import path
from aminicar.views import index,show_product



urlpatterns = [
    path('show_product', show_product , name='show_product'),
      path('index', index , name='index')
]

