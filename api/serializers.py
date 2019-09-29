from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Item, CartItem, Order


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", 'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
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

class ProfileSerializer(serializers.ModelSerializer):
    order_history = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ["id", "username", "order_history"]
    
    def get_order_history(self, obj ):
        orders = Order.objects.filter(user=obj)
        return OrderSeralizer(orders, many=True).data

class ItemSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "price", "image", "description"]

class CartDetailSeralizer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ["id", "item", "cart", "quantity", "total"]

    def get_total(self, obj):
        return obj.quantity * obj.item.price


class OrderSeralizer(serializers.ModelSerializer):
    ordered = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ["id", "status", "ordered"]

    def get_ordered(self, obj):
        items = CartItem.objects.filter(cart=obj)
        return CartDetailSeralizer(items, many=True).data


class NameImageSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "image"]

class CartItemSeralizer(serializers.ModelSerializer):
    item = NameImageSeralizer()
    class Meta:
        model = CartItem
        fields = ["id", "item", "quantity",]

class AddtoCartSeralizer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "item", "quantity"]


class UpdateCartSeralizer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "quantity"]


class ViewCartSeralizer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "cart"]




#for view cart

class Cart__Serializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ["id", "quantity", "name", "image", "price", "total"]

    def get_image(self, obj):
        image = obj.item.image.url
        return image
    
    def get_name(self, obj):
        name = obj.item.name
        return name

    def get_price(self, obj):
        price = obj.item.price
        return price

    def get_total(self, obj):
        return obj.quantity * obj.item.price

        
class Cart__2Serializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["item"]

    def get_item(self, obj):
        item = CartItem.objects.filter(cart=obj)
        return  Cart__Serializer(item, many=True).data







#for order history

class CartSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["id", "status", "item"]

    def get_item(self, obj):
        item = CartItem.objects.filter(cart=obj)
        return  CartItemSerializer(item, many=True).data



