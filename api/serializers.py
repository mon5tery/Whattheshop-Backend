from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Item, CartItem, Order




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

        # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
		# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        #
		# payload = jwt_payload_handler(new_user)
		# token = jwt_encode_handler(payload)
        #
		# validated_data["token"] = token
        return validated_data


class ItemListSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id","name", "price", "image"]

class ItemDetailSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "price", "image", "description"]

class CartDetailSeralizer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ["item", "cart", "quantity", "total"]

    def get_total(self, obj):
        return obj.quantity * obj.item.price


class OrderSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["item", "checked_out"]

class CartItemSeralizer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["item", "cart", "quantity"]