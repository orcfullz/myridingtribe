# quiz/models.py
from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    choice1 = models.CharField(max_length=100)
    choice2 = models.CharField(max_length=100)
    choice3 = models.CharField(max_length=100)
    choice4 = models.CharField(max_length=100)

class Result(models.Model):
    tribe_name = models.CharField(max_length=100)
    description = models.TextField()
    skills = models.TextField()
    strengths = models.TextField()
    weaknesses = models.TextField()
