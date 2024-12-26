from ..base.service import BaseService
from ..base.models import Order, OrderItem, Product
from ..product_service.services import ProductService
from ..payment_service.services import PaymentService
from ..shipment_service.services import ShipmentService
from django.db import transaction

class OrderService(BaseService):
    def __init__(self):
        super().__init__()
        self.product_service = ProductService()
        self.payment_service = PaymentService()
        self.shipment_service = ShipmentService()

    @transaction.atomic
    def create_order(self, user, items):
        try:
            order = Order.objects.create(
                user=user,
                total_amount=self._calculate_total(items),
                shipping_address=user.address
            )

            # Create order items with vendor
            for item in items:
                product = Product.objects.get(id=item['product_id'])
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,
                    vendor=product.vendor
                )

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