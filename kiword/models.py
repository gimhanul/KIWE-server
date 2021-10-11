from django.db import models
from user.models import User
from django.utils import timezone
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

class Usermemory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kiwe_time = models.DateTimeField(default=timezone.now)
    longestt = models.FloatField(null=True)
    longestk = models.CharField(max_length=100, null=True)
    shortestt = models.FloatField(null=True)
    shortestk = models.CharField(max_length=100, null=True)

    def __str__ (self):
        return self
    
class Each(models.Model):
    memory_id = models.ForeignKey(Usermemory, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)
    time = models.FloatField()

    def __str__ (self):
        return self