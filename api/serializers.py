from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item, CartItem, Checkout



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class ItemListSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["name", "price", "image"]

class ItemDetailSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["name", "price", "image", "description"]

class CartDetailSeralizer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ["item", "cart", "quantity", "total"]

    def get_total(self, obj):
        return obj.quantity * obj.item.price


class CheckOutSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ["item", "checked_out"]
