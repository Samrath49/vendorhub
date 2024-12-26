from rest_framework import serializers
from services.base.models import Product, Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'business_name']


class ProductSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)
    vendor_id = serializers.PrimaryKeyRelatedField(
        queryset=Vendor.objects.all(),
        write_only=True,
        source='vendor'
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price',
                  'stock', 'is_active', 'vendor', 'vendor_id']
