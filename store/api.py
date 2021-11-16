from .models import Cart
from rest_framework import viewsets, permissions
from .serializers import  CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permissions = [permissions.AllowAny]


