from ..base.service import BaseService
from .models import Payment
from django.db import transaction


class PaymentService(BaseService):
    @transaction.atomic
    def process_payment(self, order):
        try:
            payment = Payment.objects.create(
                order=order,
                amount=order.total_amount
            )
            # Add payment gateway integration here
            payment.status = 'COMPLETED'
            payment.save()
            return payment
        except Exception as e:
            self.add_error(str(e))
            return None