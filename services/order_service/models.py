from django.db import models
from services.base.models import TimeStampedModel


class Order(TimeStampedModel):
    user = models.IntegerField()  # Assuming user management is separate
    status = models.CharField(max_length=20, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['status']),
        ]

class OrderItem(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('product_service.Product', on_delete=models.PROTECT)
    vendor = models.ForeignKey('product_service.Vendor', on_delete=models.PROTECT)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
