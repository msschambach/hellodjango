from __future__ import unicode_literals

from django.db import models
import math

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # __str__ for python 3
    def __unicode__(self):
		return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def get_percentage_votes(self):
        question = self.question
        total_votes = 0

        for choice in question.choice_set.all():
            total_votes += choice.votes

        if(total_votes > 0):
            votes_ratio = float(self.votes)/float(total_votes)
            percentage_vote = votes_ratio * 100
        else:
            percentage_vote = 0

        return int(round(percentage_vote))



    # __str__ for python 3
    def __unicode__(self):
		return self.choice_text
