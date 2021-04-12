from rest_framework import serializers
from .models import Manufacturer,Department,Product,Equipment



class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['equipment_name', 'equipment_id', 'equipment_capacity', 'equipment_model', 'department', 'manufacturer']
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name']
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name']
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'product_code', 'product_strength']