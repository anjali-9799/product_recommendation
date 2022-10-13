from email.policy import default
from tkinter.tix import Tree
from django.db import models
# Create your models here.


RATING_CHOICES = (
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),

)


class Product(models.Model):
    product_name = models.CharField(max_length=120)
    categories = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quatity = models.IntegerField(default=1)
    for_sale = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=True)
    review = models.TextField(blank=True)
    rating = models.CharField(
        max_length=20,
        choices=RATING_CHOICES,
        default='0',
        blank=True,
    )

    def __str__(self):
        return self.product_name
