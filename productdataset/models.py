from django.db import models
from products.models import Product

# Create your models here.


class ProductSet(models.Model):
    name = models.CharField(max_length=70, default="")

    def __str__(self):
        return self.name


class ProductSetObject(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, db_index=True
    )
    price = models.FloatField()
    quantitydescription = models.CharField(max_length=100)
    inventory_count = models.PositiveIntegerField()
    nickname = models.CharField(max_length=70, null=True)
    nickname_check = models.BooleanField(default=False)
    productset = models.ForeignKey(ProductSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.description

    def save(self, *args, **kwargs):
        if not self.nickname_check:
            self.nickname = self.product.description
        return super(ProductSetObject).save(*args, **kwargs)
