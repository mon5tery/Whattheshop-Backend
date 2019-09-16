from django.db import models
from django.contrib.auth.models import User

class Quantity(models.Model):
    quantity = models.IntegerField()

class Cart(models.Model):
    buyer = models.OneToOneField(User, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)
    history = models.BooleanField(default = false)

class Item(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()
    category = models.CharField(max_length=15)
    created_on = models.DateTimeField()
    buyer = models.ManyToManyField(Cart)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)






    def __str__(self):
        return self.product_name
