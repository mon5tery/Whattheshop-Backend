from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Item(models.Model):
    CATEGORY_CHOICES = (
        ('$', '$'),
        ('$$', '$$'),
        ('$$$', '$$$'),
        ('$$$$', '$$$$'),
    )
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()
    category = models.CharField(max_length= 4, choices=CATEGORY_CHOICES)
    inventory= models.PositiveIntegerField()


    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('C', 'Cart'),
        ('O', 'Ordered'),
        ('D', 'Delivered'),
        ('X', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    
    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(str(self.id )+ " Cart ID: "+ str(self.cart.id) + " Item name: "+ self.item.name)



