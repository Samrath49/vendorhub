from django.db import models
from services.base.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        indexes = [models.Index(fields=['parent'])]

class Vendor(TimeStampedModel):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, default='active')
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        indexes = [models.Index(fields=['status'])]

class Product(TimeStampedModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='active')

    class Meta:
        indexes = [
            models.Index(fields=['vendor']),
            models.Index(fields=['category']),
            models.Index(fields=['status']),
        ]