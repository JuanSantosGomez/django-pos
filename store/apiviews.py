from rest_framework.views import APIView
from store.models import Cart, CartItem
from store.serializers import CartItemSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class GetCartItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, **kwargs):

        carts = get_object_or_404(Cart, pk=self.kwargs['cart'])
        cartitems = CartItem.objects.filter(cart=carts)
        serializer = CartItemSerializer(cartitems, many=True)
        return Response(serializer.data)

    def post(self, request, format=None, **kwargs):

        carts = get_object_or_404(Cart, pk=self.kwargs['cart'])

        request.data['cart'] = self.kwargs['cart']
        serializer = CartItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            # We want to return all cart objects after posting

            cartitems = CartItem.objects.filter(cart=carts)
            serializer = CartItemSerializer(cartitems, many=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemAPIDetail(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, format=None):
        cartitem = get_object_or_404(CartItem, pk=self.kwargs['pk'])
        carts = Cart.objects.get(pk=cartitem.cart.trackingnumber)
        cartitem.delete()
        carts.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
