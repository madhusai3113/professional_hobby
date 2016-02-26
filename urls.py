from django.conf.urls import url
from . import views

app_name = 'baseapp'
urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'login',views.login,name='login'),
    url(r'doLogin',views.doLogin,name='doLogin'),
    url(r'logout',views.logout,name='logout'),
    url(r'register',views.sign_up,name='sign_up'),
    url(r'doregister',views.register,name='doregister'),
    url(r'users',views.show_users,name='users'),
    url(r'connect/(?P<username>[a-z,A-Z,0-9])',views.connect,name='connect'),
]
