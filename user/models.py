from django.db import models


class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True) 
    password = models.CharField(max_length=10)
    agree = models.IntegerField()
    gender = models.CharField(max_length=1) #m=man, w=woman
    birth = models.DateField()
    phonenumber = models.CharField(max_length=10)

    def __str__(self):
        return self.id

'''
class Keyword(models.Model):
    keyword = models.CharField(max_length=100)
    tag = models.CharField(max_length=10)

class'''