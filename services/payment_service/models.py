from django.db import models
from services.base.models import TimeStampedModel


class Payment(TimeStampedModel):
    order = models.ForeignKey('order_service.Order', on_delete=models.PROTECT)
    vendor = models.ForeignKey(
        'product_service.Vendor', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='pending')
    transaction_id = models.CharField(max_length=100, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['order']),
            models.Index(fields=['vendor']),
            models.Index(fields=['status']),
        ]
