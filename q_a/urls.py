from django.urls import path
from . import views

app_name = 'q_a'

urlpatterns = [
    path('add_question', views.add_question, name='add_question'),
]
