from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import UserCreateSerializer
from rest_framework.views import APIView

from .models import Item

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class UserLoginView(APIView):
	serializer_class = UserLoginSerializer

class ItemDetailAPIView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'

class ItemView(ModelViewSet):
   queryset = Item.objects.all()
   def get_serializer_class(self):
       if self.action == 'list':
           return ItemList
       else:
           return ItemDetail
