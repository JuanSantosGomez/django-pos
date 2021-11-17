from .models import Cart, Store
from rest_framework import viewsets, permissions
from .serializers import CartSerializer, StoreSerializer
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin


class CartViewSet(viewsets.GenericViewSet, CreateModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permissions = [permissions.AllowAny]


class StoreViewSet(viewsets.GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permissions = [permissions.AllowAny]
