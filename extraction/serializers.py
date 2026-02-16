from rest_framework import serializers
from .models import ExtractionJob, ExtractedRecord

class StartExtractionSerializer(serializers.Serializer):
    api_token = serializers.CharField()

class ExtractionJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractionJob
        fields = "__all__"

class ExtractedRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedRecord
        fields = "__all__"
