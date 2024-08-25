from django.urls import path
from aminicar.views import home

urlpatterns = [
    path('', home , name='home')
]

