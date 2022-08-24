from django.urls import path
from . import views

app_name = 'q_a'

urlpatterns = [
    path('questions', views.Questions.as_view(), name='list'),  #as.view() is used for wiriting a class
    path('questions/new', views.QuestionCreateView.as_view(), name='new-question'),      
    path('questions/<int:pk>', views.QuestionDetailView.as_view(), name="question-details"),
    path('questions/<int:pk>/update', views.QuestionUpdateView.as_view(), name="question-update"),
    path('questions/<int:pk>/delete', views.QuestionDeleteView.as_view(), name="question-delete"),
    path('questions/<int:pk>/answer', views.AnswerQuestion.as_view(), name="answer"),
    path('vote/<int:pk>', views.vote_view, name='vote_post' )
]
# use python format for href to avoid prefixes