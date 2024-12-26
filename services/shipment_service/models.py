from django.db import models
from services.base.models import TimeStampedModel, Order


class Shipment(TimeStampedModel):
   order = models.ForeignKey('base.Order', on_delete=models.PROTECT, related_name='shipments')
   vendor = models.ForeignKey('product_service.Vendor', on_delete=models.PROTECT)
   tracking_number = models.CharField(max_length=100, blank=True)
   carrier = models.CharField(max_length=100, blank=True)
   status = models.CharField(max_length=20, default='pending')

   class Meta:
       indexes = [
           models.Index(fields=['order']),
           models.Index(fields=['vendor']),
           models.Index(fields=['status']),
       ]