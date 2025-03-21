from django import forms
from . import models

class CreateSymptom(forms.ModelForm):
    class Meta:
        model = models.Symptom
        fields = ['description']

class UpdateSymptom(forms.ModelForm):
    class Meta:
        model = models.Symptom
        fields = ['description']

class CreateDiagnosis(forms.ModelForm):
    class Meta:
        model = models.Diagnosis
        fields = ['symptoms', 'result']

class UpdateDiagnosis(forms.ModelForm):
    class Meta:
        model = models.Diagnosis
        fields = ['symptoms', 'result']