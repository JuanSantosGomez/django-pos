from rest_framework import serializers
from .models import ProductSetObject


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSetObject
        fields = ['id', 'nickname']
        read_only_fields = ['id', 'nickname']
