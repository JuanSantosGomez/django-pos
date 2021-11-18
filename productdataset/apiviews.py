from store.models import Cart
from .models import ProductSetObject
from products.models import Product
from .serializers import ItemSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from store.models import Cart
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ProductDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]

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
