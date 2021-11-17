from django.contrib import admin

from store.models import Cart, CartItem, Sales, Store

# Register your models here.
admin.site.register(Store)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Sales)
