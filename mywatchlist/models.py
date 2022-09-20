from platform import release
from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.CharField(max_length=50)
    title = models.TextField()
    rating = models.IntegerField()
    release_date =  models.TextField()
    review =  models.TextField()