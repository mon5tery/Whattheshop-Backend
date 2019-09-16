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
