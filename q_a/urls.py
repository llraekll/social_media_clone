from django.urls import path
from . import views

app_name = 'q_a'

urlpatterns = [
    path('add_question', views.add_question, name='add_question'),
    path('questions', views.Questions.as_view(), name='list'),  #as.view() is used for wiriting a class 
]
