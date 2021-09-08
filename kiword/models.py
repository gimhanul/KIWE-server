from django.db import models

class Keyword(models.Model):
    keyword = models.CharField(max_length=100)

    #place
    restaurant = models.BooleanField()
    school = models.BooleanField()
    cafe = models.BooleanField()
    party = models.BooleanField()

    #relationship
    some = models.BooleanField()
    lover = models.BooleanField()
    friend = models.BooleanField()
    family = models.BooleanField()

    #age
    ten = models.BooleanField()
    twenty = models.BooleanField()
    thirty = models.BooleanField()
    forty = models.BooleanField()
    fifty = models.BooleanField()
    sixty = models.BooleanField()
    

    def __str__(self):
        return self.keyword