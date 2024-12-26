from services.base.service import BaseService
from services.base.models import Product
from django.db import transaction

class ProductService(BaseService):
    def update_inventory(self, product_id, quantity, operation='decrease'):
        try:
            with transaction.atomic():
                product = Product.objects.select_for_update().get(
                    id=product_id,
                    vendor=self.context.get('vendor')
                )
                if operation == 'decrease':
                    if product.stock < quantity:
                        self.add_error("Insufficient stock")
                        return False
                    product.stock -= quantity
                else:
                    product.stock += quantity
                product.save()
                
                if product.stock <= product.low_stock_threshold:
                    self.notify_low_stock(product)
                return True
        except Product.DoesNotExist:
            self.add_error("Product not found")
            return False

    def notify_low_stock(self, product):
        # Implement notification logic
        pass