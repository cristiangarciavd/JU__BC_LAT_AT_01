from django.db import models
# Create your models here.

class Search(models.Model):
    name = models.CharField(max_length=40) # This is the input from the user, EX: 'mouse gamer'
    #last_search = models.DateTimeField(True, True, editable=False) # I think it has to be editable
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.FloatField(max_length=80)
    image_url = models.URLField(max_length=80)
    url = models.URLField(max_length=80)
    search = models.ForeignKey('Search', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


