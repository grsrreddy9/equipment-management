from rest_framework import serializers
from .models import Manufacturer, Department, Product, Equipment, Room, ProductGranulation



class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'equipment_name', 'equipment_id', 'equipment_capacity', 'equipment_model', 'department', 'manufacturer']
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id','name']
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_code', 'product_strength']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'number']

class ProductGranulationSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    room = RoomSerializer()
    class Meta:
        model = ProductGranulation
        fields = ['id', 'batch_number', 'product', 'room', 'start_time', 'end_time']

