from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()
    category = models.CharField(max_length=15)
    created_on = models.DateTimeField()

    def __str__(self):
        return self.product_name
