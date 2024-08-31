from django.urls import path
from aminicar.views import index,show_product,login_view,signup,base
  
app_name = 'aminicar'  


urlpatterns = [
    path('', index , name='index'),
    path('show_product/', show_product , name='show_product'),
      path('index', index , name='index'),
       path('signin/', login_view , name='signin'),
       path('signup/', signup , name='signup'),
        path('base/', base , name='base'),
      
       
]