from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from store.models import Cart, CartItem, Sales, Store
from store.serializers import CartItemSerializer, CartSerializer, StoreListSerializer, StoreSerializer
from rest_framework import status
from django.views import generic

# Create your views here.


class GetCartItems(APIView):
    def get(self, request, format=None, **kwargs):
        try:
            carts = Cart.objects.get(pk=self.kwargs['cart'])
        except:
            return Response('Cart not found', status=status.HTTP_400_BAD_REQUEST)

        cartitems = CartItem.objects.filter(cart=carts)
        if len(cartitems) == 0:
            return Response('No items in cart', status=status.HTTP_200_OK)
        serializer = CartItemSerializer(cartitems, many=True)
        return Response(serializer.data)

    def post(self, request, format=None, **kwargs):

        try:
            carts = Cart.objects.get(pk=self.kwargs['cart'])
        except:
            return Response('Cart not found', status=status.HTTP_400_BAD_REQUEST)

        cartitems = CartItem.objects.filter(cart=carts)
        duped = False

        for item in cartitems:
            if item.product.id == request.data['product']:

                try:
                    item.quantity += request.data['quantity']
                except:
                    return Response('Quantity not properly formatted', status=status.HTTP_400_BAD_REQUEST)
                if request.data['quantity'] <= 0:
                    return Response('Quantity cannot be less than zero', status=status.HTTP_400_BAD_REQUEST)
                item.save()

                duped = True
                carts.total = sum([i.quantity*i.price for i in cartitems])

                carts.save()
                break

        if not duped:
            request.data['cart'] = self.kwargs['cart']
            serializer = CartItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                cartitems = CartItem.objects.filter(cart=carts)
                carts.total = sum([i.quantity*i.price for i in cartitems])
                carts.save()
                serializero = CartItemSerializer(cartitems, many=True)
                return Response(serializero.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializero = CartItemSerializer(cartitems, many=True)
        return Response(serializero.data, status=status.HTTP_206_PARTIAL_CONTENT)

    def patch(self, request, format=None, **kwargs):
        try:
            cart = Cart.objects.get(pk=self.kwargs['cart'])
        except:
            return Response('Cart not found', status=status.HTTP_400_BAD_REQUEST)

        if type(list(request.data.values())[0]) == bool and len(list(request.data.values())) == 1:
            serializer = CartSerializer(
                cart, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class CartItemDetail(APIView):

    def delete(self, request, pk, format=None):
        try:
            cartitem = CartItem.objects.get(pk=pk)
        except:
            return Response('Cart item does not exist', status=status.HTTP_400_BAD_REQUEST)
        cartitem.delete()

        carts = Cart.objects.get(pk=cartitem.cart.trackingnumber)
        cartitems = CartItem.objects.filter(cart=carts)
        carts.total = sum([i.quantity*i.price for i in cartitems])

        carts.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class StoreDetail(APIView):

    def get(self, request, pk, format=None):
        store = Store.objects.get(pk=pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data)


class StoreList(APIView):

    def get(self, request, format=None):
        store = Store.objects.all()
        serializer = StoreListSerializer(store, many=True)
        return Response(serializer.data)


class CurrentCarts(generic.ListView):

    template_name = 'store/index.html'
    model = CartItem

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        new_object_list = []

        for item in context['object_list']:

            diff = [[idx, i] for idx, i in enumerate(
                new_object_list) if i['cart'] == item.cart]
            if diff:

                new_object_list[diff[0][0]]['elements'].append(item)
                new_object_list[diff[0][0]]['total'] += item.subtotal
            else:
                new_object_list.append(
                    {'cart': item.cart, 'elements': [item], 'total': item.subtotal})
        context['object_list'] = new_object_list
        return context


def convertSale(request, pk):

    try:
        cart = Cart.objects.get(pk=pk)
    except:
        return Response('Cart not found', status=status.HTTP_400_BAD_REQUEST)

    p = CartItem.objects.filter(cart=cart)

    for item in p:
        a = Sales(price=item.price, quantity=item.quantity, cart=item.cart.trackingnumber,
                  subtotal=item.subtotal, description=item.description)
        a.save()
        p.delete()

    cart.delete()

    return redirect('index')


class SalesView(generic.ListView):

    template_name = 'store/sales.html'
    model = Sales
