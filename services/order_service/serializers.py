from rest_framework import serializers
from ..base.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price', 'vendor']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'total_amount', 'status', 'shipping_address', 'created_at', 'updated_at', 'items']
    
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.status = validated_data.get('status', instance.status)
        instance.shipping_address = validated_data.get('shipping_address', instance.shipping_address)
        instance.save()

        # Update nested items
        items_data = validated_data.pop('items', None)
        if items_data:
            # Delete existing items
            instance.items.all().delete()

            # Re-create the items with the new data
            for item_data in items_data:
                OrderItem.objects.create(order=instance, **item_data)

        return instance