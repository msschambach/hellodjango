from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime
from rest_framework import generics
from polls.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
# Create your views here.


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
