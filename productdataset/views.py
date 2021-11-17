from store.models import Cart, Store
from .models import ProductSet, ProductSetObject
from products.models import Product
from .serializers import ItemSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from store.models import Cart
from store.models import Store
# Create your views here.


class ProductDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, barcode, cart):
        try:
            produce = Product.objects.get(barcode=barcode)

            carter = Cart.objects.filter(sold=False).get(pk=cart)
            store = carter.store
            productsets = store.productset
            return ProductSetObject.objects.filter(product=produce).get(productset=productsets)
        except ProductSetObject.DoesNotExist:
            raise Http404

    def get(self, request, format=None, **kwargs):
        product = self.get_object(
            barcode=kwargs["barcode"], cart=kwargs["cart"])
        serializer = ItemSerializer(product)

        return Response(serializer.data)
