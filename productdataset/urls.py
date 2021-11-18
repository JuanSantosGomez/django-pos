from .apiviews import ProductDetail
from django.urls import path

urlpatterns = [
    path("product/check/<barcode>/<cart>", ProductDetail.as_view()),
]
