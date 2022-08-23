from turtle import title
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.


@login_required(login_url='signin')
def add_question(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        title = request.POST['title']
        description = request.POST['description']

        new_query = Question.objects.create(user=user, image=image, title=title, description=description)
        new_query.save()

        return redirect('/')
    else:
        return redirect('/')

class Questions(ListView):
    model= Question
    template_name = 'question_list.html' # template_name must be mentioned for class based views in django
    context_object_name = 'questions' # this is the name used for looping in html and for the .title & .description
    ordering = ['-created_at']

class QuestionDetailView(DetailView):
    model= Question
    template_name = 'question_detail.html'

class QuestionCreateView(CreateView):
    model = Question
    fields =['title', 'description', 'image']
    template_name = 'question_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 