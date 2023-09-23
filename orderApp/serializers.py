from rest_framework import serializers
from .models import Order, Shipment

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['id_reference', 'order', 'order_id', 'address', 'owner_name', 'owner_email', 'shipment_date', 'status_info']

class OrderSerializer(serializers.ModelSerializer):
    shipment = ShipmentSerializer()

    class Meta:
        model = Order
        fields = ['name', 'quantity', 'price', 'weight', 'created_at']
        
    def create(self, validated_data):
        try:
            order = Order.objects.get(id=validated_data['order_id'])
            shipment = Shipment.objects.create(
                order=order,
                **validated_data,
            )
            
            return shipment
        except Order.DoesNotExist:
            raise serializers.ValidationError('Order does not exist')    