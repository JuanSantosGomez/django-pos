from re import I
from rest_framework import routers

from store.views import GetCartItems
from .api import CartViewSet
from .views import CartItemDetail, CurrentCarts, SalesView, StoreDetail, StoreList, convertSale
from django.urls import path

router = routers.DefaultRouter()
router.register("api/store/carts", CartViewSet, "carts")

urlpatterns = [

    # The scanner app API Views

    path('api/store/cartitems/<cart>',
         GetCartItems.as_view(), name='getcartitems'),
    path('api/store/cartitems/items/<pk>',
         CartItemDetail.as_view(), name='cartitems'),
    path('api/store/<pk>',
         StoreDetail.as_view(), name='store'),
    path('api/store/',
         StoreList.as_view(), name='storelist'),


    # The stores app views

    path('site/store/', CurrentCarts.as_view(), name='index'),

    path('convert/sale/<pk>', convertSale, name='convertsale'),

    path('sales', SalesView.as_view(), name='sales'),

]
urlpatterns += router.urls
