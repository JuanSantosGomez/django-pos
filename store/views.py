from rest_framework.views import APIView
from rest_framework.response import Response
from store.models import Cart, CartItem
from store.serializers import CartItemSerializer
from rest_framework import status

# Create your views here.


class GetCartItems(APIView):
    def get(self, request, format=None, **kwargs):
        carts = Cart.objects.get(pk=self.kwargs['cart'])
        cartitems = CartItem.objects.filter(cart=carts)
        serializer = CartItemSerializer(cartitems, many=True)
        return Response(serializer.data)

    def post(self, request, format=None, **kwargs):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemDetail(APIView):

    def delete(self, request, pk, format=None):
        cartitem = self.get_object(pk)
        cartitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
