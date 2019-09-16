from rest_framework.generics import CreateAPIView
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from .models import Item

class ItemView(ModelViewSet):
    queryset = Item.objects.all()


    def get_serializer_class(self):
        if self.action == 'list':
            return ItemList
        else:
            return ItemDetail




class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
