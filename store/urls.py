from re import I
from rest_framework import routers
from .api import CartViewSet

from django.urls import path

router = routers.DefaultRouter()
router.register("api/store/carts", CartViewSet, "carts")
urlpatterns = router.urls
