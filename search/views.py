from turtle import title
from django.shortcuts import render
from users.models import User, Profile
from itertools import chain
from q_a.models import Question

# Create your views here.
def search_user(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)
        
        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'search.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list})

def search_title (request):
    title_object = Question.objects.get(title=request.question.title)
    title_searched = Question.objects.get(title=title_object)

    if request.method == 'POST':
        title = request.POST['title']
        question_title = Question.objects.filter(title__icontains=title)

        title_search = []
        title_search_list = []

        for titles in question_title:
            title_search.append(titles.id)

        for ids in title_search:
            title_lists = Question.objects.filter(id=ids)
            title_search_list.append(title_lists)
        
        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'search.html', {'title_searched': title_searched, 'title_search_list': title_search_list})