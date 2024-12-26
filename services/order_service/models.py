from django.db import models
from django.core.validators import MinValueValidator
from services.base.models import TimeStampedModel, Order as BaseOrder, OrderItem as BaseOrderItem


class OrderService(TimeStampedModel):
    """Extended order functionality specific to order service"""
    order = models.OneToOneField(
        BaseOrder, on_delete=models.CASCADE, related_name='order_service')
    shipping_method = models.CharField(max_length=50)
    estimated_delivery = models.DateTimeField(null=True)
    notes = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['estimated_delivery']),
        ]


class OrderTracking(TimeStampedModel):
    """Track order status changes"""
    order = models.ForeignKey(
        BaseOrder, on_delete=models.CASCADE, related_name='tracking_history')
    status = models.CharField(max_length=20, choices=BaseOrder.STATUS_CHOICES)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']
