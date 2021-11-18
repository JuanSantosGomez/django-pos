from .models import Cart, Store
from rest_framework import viewsets
from .serializers import CartSerializer, StoreSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]


class StoreViewSet(viewsets.GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]
