from rest_framework import serializers
from .models import Symptom, Diagnosis

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ['description', 'author', 'date']

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ['symptoms', 'result', 'author', 'date']