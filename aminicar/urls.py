from django.urls import path
from aminicar.views import index,show_product,login_view,signup
  
app_name = 'aminicar'


urlpatterns = [
    path('show_product/', show_product , name='show_product'),
      path('', index , name='index'),
       path('signin/', login_view , name='signin'),
       path('signup/', signup , name='signup')
]