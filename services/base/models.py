from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    is_vendor = models.BooleanField(default=False)

class Vendor(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    commission_rate = models.DecimalField(
        max_digits=5, decimal_places=2, default=10.00)
    payment_details = models.JSONField(default=dict)

    def __str__(self):
        return self.business_name


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'


class Product(TimeStampedModel):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['vendor', 'category']),
        ]


class Order(TimeStampedModel):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='PENDING')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['user', 'status']),
        ]


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['order', 'vendor']),
        ]


class Payment(TimeStampedModel):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='payments')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='PENDING')
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_method = models.CharField(max_length=50)


class Shipment(TimeStampedModel):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered'),
    ]

    order_item = models.ForeignKey(
        OrderItem, on_delete=models.CASCADE, related_name='shipments')
    tracking_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='PENDING')
    carrier = models.CharField(max_length=100)
    estimated_delivery = models.DateField(null=True, blank=True)
