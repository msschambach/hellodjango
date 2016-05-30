from rest_framework import serializers
from polls.models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        field = ('id','question_text','pub_date')


class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Choice
        field = ('id','question','choice_text','votes')
