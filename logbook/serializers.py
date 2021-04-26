from rest_framework import serializers
from .models import LogBook, CleanType
from Main.serializers import ProductGranulationSerializer

class CleanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleanType
        fields = ['id', 'clean_type']

class LogBookSerializer(serializers.ModelSerializer):
    product_details = ProductGranulationSerializer()
    clean_type = CleanTypeSerializer()
    class Meta:
        model = LogBook
        fields = ['id','qa_checked_by', 'qa_checked_on', 'product_details',  'clean_type', 'equipment_cleaned_on', 'room_cleaned_on', 'equipment_clean_done_by', 'room_clean_done_by', 'cleaning_checked_by']
