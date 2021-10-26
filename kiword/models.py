from django.db import models
from user.models import User
from django.utils import timezone
from django.db.models.deletion import CASCADE



#question and choice model
class Question(models.Model):
    question = models.CharField(max_length = 200)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=10)

    def __str__(self):
        return self.choice



#keyword model
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



#memory model
class Usermemory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kiwe_time = models.DateTimeField(default=timezone.now)
    longestk = models.CharField(max_length=100, null=True)

    def __str__ (self):
        return self

def wordcloud_directory_path():
    return 0

class Each(models.Model):
    memory = models.ForeignKey(Usermemory, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)
    time = models.FloatField()

    def __str__ (self):
        return self

class Memorytype(models.Model):
    highlighter = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    order = models.BooleanField(default=False)

    def __str__ (self):
        return self.highlighter

class Memoryresult(models.Model):
    memory = models.ForeignKey(Usermemory, on_delete=models.CASCADE)
    mt = models.ForeignKey(Memorytype, on_delete=models.CASCADE)
    result = models.CharField(max_length=20, null=True)

    def __str__ (self):
        return self