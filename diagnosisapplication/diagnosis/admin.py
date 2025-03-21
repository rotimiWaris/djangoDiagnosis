from django.contrib import admin
from .models import Diagnosis, Symptom

# Register your models here.
admin.site.register(Diagnosis)
admin.site.register(Symptom)