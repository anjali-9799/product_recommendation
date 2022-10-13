from email.policy import default
from itertools import product
from django.db import models
from products.models import Product

# Create your models here.


class Orders(models.Model):
    PLACED = 'PL'
    INTRANSIT = 'IT'
    DELIVERED = 'DL'
    DELAYED = 'DA'
    RETURNED = 'RE'
    ORDER_STATUS = [
        (PLACED, 'Placed'),
        (INTRANSIT, 'InTransit'),
        (DELIVERED, 'Delivered'),
        (DELAYED, 'Delayed'),
        (RETURNED, 'Returned'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.CharField(
        max_length=2, choices=ORDER_STATUS, default=PLACED)
