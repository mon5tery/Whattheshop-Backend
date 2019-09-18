from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Quantity(models.Model):
   quantity = models.IntegerField()

class Cart(models.Model):
   buyer = models.OneToOneField(User, on_delete=models.CASCADE)
   quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)
   history = models.BooleanField(default = false)

class Item(models.Model):

    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()
    category = models.CharField(max_length=15)


    def __str__(self):
        return self.name.id


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checked_out = models.DateTimeField()


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Checkout, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
