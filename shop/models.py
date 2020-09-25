from django.db import models

class Seed(models.Model):
    ''' Seed model '''

    name = models.CharField(max_length=25, unique=True)
    picture = models.ImageField()
    title = models.CharField(max_length=50)
    short_description = models.TextField()
    logn_description = models.TextField()
