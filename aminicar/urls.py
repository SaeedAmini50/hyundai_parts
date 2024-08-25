from django.urls import path
from aminicar.views import index

urlpatterns = [
    path('index', index , name='index')
]

