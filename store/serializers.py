from rest_framework.fields import ReadOnlyField
from productdataset.models import ProductSetObject
from rest_framework import serializers


from store.models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'cart', 'price', 'description']
