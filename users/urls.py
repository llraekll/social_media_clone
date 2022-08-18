from django.urls import  path
from . import views as user_views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('user/signup', user_views.signup, name='signup'),
    path('user/signin', auth_views.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('user/signout', auth_views.LogoutView.as_view(template_name='signout.html'), name='signout'),
    path('user/profile', user_views.profile, name='profile'),
]
