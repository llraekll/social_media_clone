from turtle import title
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question

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
