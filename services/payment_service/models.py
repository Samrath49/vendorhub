from django.db import models
from services.base.models import TimeStampedModel, Order


class Payment(TimeStampedModel):
    order = models.ForeignKey(
         'base.Order', on_delete=models.CASCADE, related_name='service_payments')
    vendor = models.ForeignKey('base.Vendor', on_delete=models.CASCADE, related_name='service_payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=Order.STATUS_CHOICES, default='PENDING')
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_method = models.CharField(max_length=50)

    class Meta:
        indexes = [
            models.Index(fields=['order']),
            models.Index(fields=['vendor']),
            models.Index(fields=['status']),
        ]
