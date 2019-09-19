
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from .models import Item, CartItem, Order

class ItemView(ModelViewSet):
    queryset = Item.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ItemListSeralizer
        else:
            return ItemDetailSeralizer

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class CartItemCreateAPIView(CreateAPIView):
    serializer_class = CartItemSeralizer

