from django.db import models
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.FloatField(max_length=80)
    image_url = models.URLField(max_length=80)
    url = models.URLField(max_length=80)