from random import choice
from annotated_types import MaxLen
from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=5000)

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice = models.CharField(max_length=50000)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice