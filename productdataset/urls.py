from re import I
from rest_framework import urlpatterns
from .views import ProductDetail
from django.urls import path

urlpatterns = [
    path("product/check/<barcode>/<productset>", ProductDetail.as_view()),
]
