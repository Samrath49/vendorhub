from ..base.service import BaseService
from .models import Shipment
from django.db import transaction


class ShipmentService(BaseService):
    @transaction.atomic
    def create_shipment(self, order):
        try:
            shipment = Shipment.objects.create(
                order=order,
                status='PENDING'
            )
            return shipment
        except Exception as e:
            self.add_error(str(e))
            return None

    def update_shipment_status(self, shipment_id, status):
        try:
            shipment = Shipment.objects.get(id=shipment_id)
            shipment.status = status
            shipment.save()
            return shipment
        except Shipment.DoesNotExist:
            self.add_error("Shipment not found")
            return None