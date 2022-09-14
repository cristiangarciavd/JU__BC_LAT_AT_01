from django.db import models
from datetime import date

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.FloatField(max_length=80)
    image_url = models.URLField(max_length=80)
    url = models.URLField(max_length=80)
    search = models.ForeignKey('Search', on_delete=models.CASCADE)
    origin = models.CharField(max_length=80)
    
    def __str__(self):
        return self.name

class Search(models.Model):
    name = models.CharField(max_length=40) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    times_searched = models.IntegerField(default=1)

    def __str__(self):
        return self.name
        



