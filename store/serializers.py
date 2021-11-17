from rest_framework import serializers
from store.models import Cart, CartItem, Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
        read_only_fields = ['id', 'name', 'productset']


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['store', 'sold', 'total', 'trackingnumber']
        read_only_fields = ['total', 'trackingnumber']


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'id', 'cart', 'price', 'description']
        read_only_fields = ['id', 'price', 'description']
