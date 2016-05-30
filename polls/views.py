from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime
from .models import Question, Choice

# Create your views here.
title = "Polls"

def index(request):
    title = "Questions"
    latest_questions = Question.objects.order_by('-pub_date')[:10]

    return render(request, 'polls/index.html',{'questions':latest_questions,'title':title})

def single_poll(request, question_id):
    title = "Single Poll"
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/single_poll.html',{'question':question,'title':title})

def single_poll_vote(request, question_id):
    title = "Single Poll Vote"
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/single_poll_vote.html',{'question':question,'title':title})

def single_poll_save_vote(request, question_id):
    choice_id = request.POST.get('choice_id')
    choice = Choice.objects.get(id=choice_id)
    choice.votes  = choice.votes + 1
    choice.save()

    return redirect('single_poll',question_id)


def create_poll(request):
    title = "New Poll"
    return render(request, 'polls/new_poll_form.html',{'title':title})

def save_poll(request):
    question = request.POST.get('question')
    choices = request.POST.get('choices').split(',')

    question_object = Question()
    question_object.question_text = question
    question_object.pub_date = datetime.now()
    question_object.save()

    for choice in choices:
        choice_object = Choice()
        choice_object.choice_text = choice
        choice_object.question = question_object
        choice_object.votes = 0
        choice_object.save()

    return redirect('polls_index')
