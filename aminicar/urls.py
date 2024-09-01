from django.urls import path
from aminicar.views import (index,
show_product,
register_signin,
register_signup,
base,indexAdmin,
logout_view)
  
app_name = 'aminicar'  


urlpatterns = [
    path('', index , name='index'),
    path('show_product/', show_product , name='show_product'),
      path('index', index , name='index'),
        path('signin/', register_signin , name='signin'),
       path('signup/', register_signup , name='signup'),
        path('base/', base , name='base'),
        path('logout/', logout_view , name='logout'),
         path('indexAdmin/', indexAdmin , name='indexAdmin')

]