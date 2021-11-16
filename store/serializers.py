from django.db import models
from django.db.models import fields
from rest_framework import serializers

from store.models import Cart


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'
