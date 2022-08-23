from turtle import title
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Answer, Question
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .forms import AnswerForm
from django.urls import reverse_lazy


# Create your views here.





class Questions(ListView):
    model = Question
    # template_name must be mentioned for class based views in django
    template_name = 'question_list.html'
    # this is the name used for looping in html and for the .title & .description
    context_object_name = 'questions'
    ordering = ['-created_at']


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question_detail.html'


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'description', 'image']
    template_name = 'question_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class QuestionUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['title', 'description', 'image']
    template_name = 'question_update.html'

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        else:
            return False


class QuestionDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'question_confirm_delete.html'
    ontext_object_name = 'questions'
    success_url = '/'

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        else:
            return False


class AnswerDetailView(DetailView):
    model= Answer
    from_class = AnswerForm
    template_name = 'question_detail.html'

    def form_vaild(self, form):
        form.instance.question.id = self.kwargs['pk']
        return super().form_vaild(form)
    success_url = reverse_lazy('q_a:question-detail')

class AnswerQuestion(CreateView):
    model= Answer
    form_class=AnswerForm
    template_name = 'question-answer.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('q_a:list')

