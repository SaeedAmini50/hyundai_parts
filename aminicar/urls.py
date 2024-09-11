from django.urls import path
from aminicar.views import (index,
show_product,
register_signin,
register_signup,
base,indexAdmin,
H2630035505,
H319102H000,
H2351025250,
H311121R000,
H273012B010,
H3C10028164,
errorpage,
edit_account_view,
not_find,

logout_view)
  
app_name = 'aminicar'  


urlpatterns = [
    
    path('show_product/', show_product , name='show_product'),
      path('index', index , name='index'),
        path('signin/', register_signin , name='signin'),
       path('signup/', register_signup , name='signup'),
        path('base/', base , name='base'),
       
         path('H2630035505/', H2630035505 , name='H2630035505'),
       path('H319102H000/', H319102H000 , name='H319102H000'),
       path('H2351025250/', H2351025250 , name='H2351025250'),
       path('H311121R000/', H311121R000 , name='H311121R000'),
       path('H273012B010/', H273012B010 , name='H273012B010'),
       path('H3C10028164/', H3C10028164 , name='H3C10028164'),
       path('logout/', logout_view , name='logout'),
      path('errorpage/', errorpage , name='errorpage'),
       path('not_find/', not_find , name='not_find'),
         path('indexAdmin/', indexAdmin , name='indexAdmin'),
           path('<user_id>/profile/', edit_account_view , name='profile')

]