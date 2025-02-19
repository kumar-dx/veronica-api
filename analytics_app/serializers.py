from rest_framework import serializers
from .models import VisitorRecord

class VisitorRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorRecord
        fields = ['id', 'store_id', 'date', 'unique_visitors']
