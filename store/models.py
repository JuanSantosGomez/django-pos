from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import ForeignKey


from productdataset.models import ProductSet, ProductSetObject
# Create your models here.
import uuid


def make_uuid():
    return str(uuid.uuid4())


class UUIDModel(models.Model):

    trackingnumber = models.CharField(primary_key=True,
                                      editable=False, max_length=36, db_index=True,
                                      unique=True, default=make_uuid
                                      )

    class Meta:
        abstract = True


class Store(models.Model):
    name = models.CharField(max_length=100, null=True)
    productset = models.ForeignKey(ProductSet, on_delete=SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"


class Cart(UUIDModel):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.trackingnumber}"


class CartItem(models.Model):
    product = models.ForeignKey(
        ProductSetObject, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(null=True, default=0.0)
    quantity = models.PositiveIntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart-{self.cart.trackingnumber} - {self.product.product.description}"

    def save(self, *args, **kwargs) -> None:
        self.price = self.product.price
        return super(CartItem, self).save(args, kwargs)
