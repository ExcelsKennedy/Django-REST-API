from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    # author 
    # title 
    # date published 
    # date edited 
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False) 
    title = models.CharField(max_length=100, blank=False) 
    date_published = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['-date_published'] 

class Answer(models.Model):
    # question 
    # choices 
    # date_published 
    # date_edited 
    quiz = models.ForeignKey(Question, on_delete=models.CASCADE, editable=False)
    choices = models.CharField(max_length=30, blank=False)
    date_published = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['-date_published'] 