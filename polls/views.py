from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.
title = "Polls"

def index(request):
    title = "Questions"
    latest_questions = Question.objects.order_by('-pub_date')[:10]
    return render(request, 'polls/index.html',{'questions':latest_questions,'title':title})
