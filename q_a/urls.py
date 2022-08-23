from django.urls import path
from . import views

app_name = 'q_a'

urlpatterns = [
    path('questions/new', views.QuestionCreateView.as_view(), name='new-question'),
    path('questions', views.Questions.as_view(), name='list'),  #as.view() is used for wiriting a class 
    path('questions/<int:pk>', views.QuestionDetailView.as_view(), name="question-details"),
    path('questions/<int:pk>/update', views.QuestionUpdateView.as_view(), name="question-update"),
    path('questions/<int:pk>/delete', views.QuestionDeleteView.as_view(), name="question-delete"),
]
