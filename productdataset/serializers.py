from rest_framework import serializers
from .models import ProductSetObject


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSetObject
        fields = "__all__"
