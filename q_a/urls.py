from django.urls import path
from . import views

urlpatterns = [
    path('qa/post_query', views.post_query, name='post_query'),
]
