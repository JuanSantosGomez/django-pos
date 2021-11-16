from rest_framework.views import APIView
from rest_framework.response import Response
from store.models import Cart, CartItem
from store.serializers import CartItemSerializer, CartSerializer
from rest_framework import serializers, status

# Create your views here.


class GetCartItems(APIView):
    def get(self, request, format=None, **kwargs):
        carts = Cart.objects.get(pk=self.kwargs['cart'])
        cartitems = CartItem.objects.filter(cart=carts)
        serializer = CartItemSerializer(cartitems, many=True)
        return Response(serializer.data)

    def post(self, request, format=None, **kwargs):
        carts = Cart.objects.get(pk=self.kwargs['cart'])
        cartitems = CartItem.objects.filter(cart=carts)
        duped = False
        for item in cartitems:
            if item.id == request.data['product']:
                item.quantity += request.data['quantity']
                item.save()
                duped = True

        serializero = CartItemSerializer(cartitems, many=True)

        if not duped:
            serializer = CartItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializero.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializero.data, status=status.HTTP_206_PARTIAL_CONTENT)

    def patch(self, request, format=None, **kwargs):
        cart = Cart.objects.get(pk=self.kwargs['cart'])
        if type(list(request.data.values())[0]) == bool and len(list(request.data.values())) == 1:
            serializer = CartSerializer(
                cart, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class CartItemDetail(APIView):

    def delete(self, request, pk, format=None):
        cartitem = CartItem.objects.get(pk=pk)
        cartitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
