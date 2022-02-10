from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    #account = models.OneToOneField(Product, on_delete=models.CASCADE)

class DateOfManufacture(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
