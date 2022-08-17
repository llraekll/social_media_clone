from django.urls import path
from . import views

urlpatterns = [
    path('qa/add_question', views.add_question, name='add_question'),
]
