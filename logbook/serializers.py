from rest_framework import serializers
from .models import LogBook, CleanType, CleaningDetail
from Main.serializers import ProductGranulationSerializer

class CleanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleanType
        fields = ['id', 'clean_type']

class CleaningDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningDetail
        fields = ['id', 'clean_type', 'equipment_cleaned_by', 'equipment_cleaned_on', 'room_cleaned_by', 'room_cleaned_on', 'product_details']

class LogBookSerializer(serializers.ModelSerializer):
    product_details = ProductGranulationSerializer()
    cleaning_details = CleaningDetailSerializer()
    class Meta:
        model = LogBook
        fields = ['id','qa_checked_by', 'qa_checked_on', 'product_details', 'cleaning_details', 'cleaning_checked_by', 'cleaning_checked_on']
