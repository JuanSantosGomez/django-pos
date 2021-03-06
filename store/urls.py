from re import I
from rest_framework import routers

from store.views import GetCartItems
from .api import CartViewSet
from .views import CartItemDetail, StoreDetail, StoreList
from django.urls import path

router = routers.DefaultRouter()
router.register("api/store/carts", CartViewSet, "carts")

urlpatterns = [
    path('api/store/cartitems/<cart>',
         GetCartItems.as_view(), name='getcartitems'),
    path('api/store/cartitems/items/<pk>',
         CartItemDetail.as_view(), name='cartitems'),
    path('api/store/<pk>',
         StoreDetail.as_view(), name='store'),
    path('api/store/',
         StoreList.as_view(), name='storelist'),


]
urlpatterns += router.urls
