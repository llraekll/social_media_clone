from django.shortcuts import get_object_or_404
from .models import Answer, Question
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .forms import AnswerForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# Create your views here.


def vote_view_question(request, pk):
    post = get_object_or_404(Question, id=request.POST.get('question_id'))
    voted = False
    if post.votes.filter(id=request.user.id).exists():  #votes here is the model class
        post.votes.remove(request.user)
        voted = False
    else:
        post.votes.add(request.user)
        voted = True
    return HttpResponseRedirect(reverse('q_a:question-details', args=[str(pk)]))

# def vote_view_answer(request, pk):
#     post = get_object_or_404(Answer, id=request.POST.get('answer_id'))
#     voted = False
#     if post.votes.filter(id=request.user.id).exists():  #votes here is the model class
#         post.votes.remove(request.user)
#         voted = False
#     else:
#         post.votes.add(request.user)
#         voted = True
#     return HttpResponseRedirect(reverse('q_a:question-details', args=[str(pk)]))


class Questions(ListView):
    model = Question
    # template_name must be mentioned for class based views in django V
    template_name = 'question_list.html'
    # this is the name used for looping in html and for the .title & .description V
    context_object_name = 'questions'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context['questions'] = context['questions'].filter(title__icontains = search_input)
            context['search_input'] = search_input
        return context


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(QuestionDetailView, self).get_context_data()
        vote_data = get_object_or_404(Question, id=self.kwargs['pk'])
        total_votes = vote_data.total_votes()
        voted = False
        if vote_data.votes.filter(id=self.request.user.id).exists():
            voted = True

        context['total_votes'] = total_votes
        context['voted'] = voted
        return context
        
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context['questions'] = context['questions'].filter(title__icontains = search_input)
            context['search_input'] = search_input
        return context

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
    model = Answer
    from_class = AnswerForm
    template_name = 'question_detail.html'

    def form_vaild(self, form):
        form.instance.question.id = self.kwargs['pk']
        return super().form_vaild(form)
    success_url = reverse_lazy('q_a:question-detail')

    # def get_context_data(self, *args, **kwargs):
    #     context = super(AnswerDetailView, self).get_context_data()
    #     vote_data = get_object_or_404(Answer, id=self.kwargs['pk'])
    #     total_vote = vote_data.total_votes()
    #     voted = False
    #     if vote_data.votes.filter(id=self.request.user.id).exists():
    #         voted = True

    #     context['total_votes'] = total_vote
    #     context['voted'] = voted
    #     return context


class AnswerQuestion(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'question-answer.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('q_a:list')
