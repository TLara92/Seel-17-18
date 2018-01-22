from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import QuestionForm, AnswerForm
from .models import Question, PageType, Answer
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied


def information(request):
    if request.method == 'GET':
        q_form = QuestionForm()
        a_form = AnswerForm()
        return render(request, 'info.html', {'q_form': q_form, 'a_form': a_form, 'questions': Question.get_questions(PageType.INFO_PAGE)})


def post_question(request):
    if request.method == 'POST':
        if 'question_button' in request.POST:
            q_form = QuestionForm(request.POST)
            if q_form.is_valid():
                if(request.user.is_authenticated):
                    Question.create_question(q_form.cleaned_data['question'], PageType.INFO_PAGE, request.user)
                else:
                    Question.create_question(q_form.cleaned_data['question'], PageType.INFO_PAGE)
    return HttpResponseRedirect(reverse('information'))


def post_answer(request):
    if request.method == 'POST':
        if 'answer_button' in request.POST:
            a_form = AnswerForm(request.POST)
            if a_form.is_valid():
                if(a_form.cleaned_data['answer_from']):
                    q = Question.get_question(a_form.cleaned_data['answer_from'])
                    if(request.user.is_authenticated):
                        q.add_answer(a_form.cleaned_data['answer'], request.user)
                    else:
                        q.add_answer(a_form.cleaned_data['answer'])
    return HttpResponseRedirect(reverse('information'))


def has_permission(user):
    if user:
        return user.groups.filter(name='administrators').exists() or user.groups.filter(name='moderators').exists()
    return False


@login_required
@user_passes_test(has_permission)
def delete_question(request):
    if request.method == 'POST':
        q_id = request.POST.get('q_id')
        if q_id:
            q = Question.get_question(q_id)
            q.delete_question()
    return HttpResponseRedirect(reverse('information'))


@login_required
def delete_answer(request):
    if request.method == 'POST':
        a_id = request.POST.get('a_id')
        if a_id:
            a = Answer.get_answer(a_id)
            if a.user == request.user or has_permission(request.user):
                a.delete_answer()
            else:
                raise PermissionDenied
    return HttpResponseRedirect(reverse('information'))


@login_required
@user_passes_test(has_permission)
def edit_question(request):
    if request.method == 'POST':
        q_form = QuestionForm(request.POST)
        q_id = request.POST.get('q_id')
        if q_form.is_valid() and q_id:
            q = Question.get_question(q_id)
            q.edit_question(q_form.cleaned_data['question'])
    return HttpResponseRedirect(reverse('information'))


@login_required
def edit_answer(request):
    if request.method == 'POST':
        a_form = AnswerForm(request.POST)
        if a_form.is_valid():
            a = Answer.get_answer(a_form.cleaned_data['answer_id'])
            if a.user == request.user or has_permission(request.user):
                a.edit_answer(a_form.cleaned_data['answer'])
            else:
                raise PermissionDenied
    return HttpResponseRedirect(reverse('information'))