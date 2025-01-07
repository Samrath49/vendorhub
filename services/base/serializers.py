from rest_framework import serializers
from .models import Vendor, User

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'business_name', 'description', 'is_active', 
                 'commission_rate', 'payment_details', 'user']
        read_only_fields = ['user']