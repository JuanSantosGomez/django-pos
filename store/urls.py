from re import I
from rest_framework import routers

from .apiviews import CartItemAPIDetail, GetCartItemsView, CartDeleteView
from .apiviewsets import CartViewSet, StoreViewSet
from .views import CurrentCarts, SalesView, convertSale
from django.urls import path

router = routers.DefaultRouter()
router.register("api/cart", CartViewSet, "cartsAPI")
router.register("api/store", StoreViewSet, "storeAPI")

urlpatterns = [

    # The scanner app API Views

    path('api/cartitems/items/<pk>',
         CartItemAPIDetail.as_view(), name='cartitemdetailsAPI'),
    path('api/cartitems/<cart>',
         GetCartItemsView.as_view(), name='cartitemsAPI'),
    path('api/cart/<pk>',
         CartDeleteView.as_view(), name='cartdeleteAPI'),


    # The stores app views

    path('site/store/', CurrentCarts.as_view(), name='index'),

    path('convert/sale/<pk>', convertSale, name='convertsale'),

    path('sales', SalesView.as_view(), name='sales'),

]

urlpatterns += router.urls
