from django.db import models
from user.models import User
from django.db.models.deletion import CASCADE

class Question(models.Model):
    question = models.CharField(max_length = 200)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=10)

    def __str__(self):
        return self.choice


class Keyword(models.Model):
    keyword = models.CharField(max_length = 100)

    def __str__(self):
        return self.keyword 


class KeywordRelated(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    question = models.CharField(max_length=2)
    choice = models.CharField(max_length=2)

    def __str__(self):
        return self.choice

class Userchoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
