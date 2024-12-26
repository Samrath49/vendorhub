from ..base.service import BaseService
from .models import Product
from django.db import transaction


class ProductService(BaseService):
    def update_inventory(self, product_id, quantity, operation='decrease'):
        try:
            with transaction.atomic():
                product = Product.objects.select_for_update().get(id=product_id)
                if operation == 'decrease':
                    if product.stock < quantity:
                        self.add_error("Insufficient stock")
                        return False
                    product.stock -= quantity
                else:
                    product.stock += quantity
                product.save()
                return True
        except Product.DoesNotExist:
            self.add_error("Product not found")
            return False

    def check_low_stock(self, product_id):
        product = Product.objects.get(id=product_id)
        if product.stock <= product.low_stock_threshold:
            # Send notification instead of signal
            self.notify_low_stock(product)
