from django.contrib import admin
from .models import SalesOrder
from .models import DateOfManufacture

admin.site.register(SalesOrder)
admin.site.register(DateOfManufacture)
