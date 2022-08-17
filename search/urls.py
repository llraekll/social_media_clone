from django.urls import  path
from . import views

app_name = 'search'

urlpatterns = [
    path('search_user', views.search_user, name='search_user'),
    path('search_title', views.search_title, name='search_title'),
]
