from ..base.service import BaseService
from .models import Order
from ..product_service.services import ProductService
from ..payment_service.services import PaymentService
from ..shipment_service.services import ShipmentService
from django.db import transaction
from .models import Product


class OrderService(BaseService):
    def __init__(self):
        super().__init__()
        self.product_service = ProductService()
        self.payment_service = PaymentService()
        self.shipment_service = ShipmentService()

    @transaction.atomic
    def create_order(self, user, items):
        try:
            # Validate stock
            for item in items:
                if not self.product_service.update_inventory(
                    item['product_id'], 
                    item['quantity']
                ):
                    raise Exception("Stock update failed")

            # Create order
            order = Order.objects.create(
                user=user,
                total_amount=self._calculate_total(items)
            )

            # Process payment
            payment = self.payment_service.process_payment(order)
            if not payment:
                raise Exception("Payment failed")

            # Create shipment
            shipment = self.shipment_service.create_shipment(order)
            if not shipment:
                raise Exception("Shipment creation failed")

            return order

        except Exception as e:
            self.add_error(str(e))
            return None

    def _calculate_total(self, items):
        total = 0
        for item in items:
            product = Product.objects.get(id=item['product_id'])
            total += product.price * item['quantity']
        return total