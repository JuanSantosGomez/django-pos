from django.shortcuts import redirect
from rest_framework.response import Response
from store.models import Cart, CartItem, Sales
from rest_framework import status
from django.views import generic

# Create your views here.


class SalesView(generic.ListView):

    template_name = 'store/sales.html'
    model = Sales


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
