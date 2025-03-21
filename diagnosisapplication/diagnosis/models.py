from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from diagnosisapp.utils import unique_slug_generator, unique_slug_generator_for_diagnosis

# Create your models here.

class Symptom(models.Model):
    description = models.TextField()
    slug =  models.SlugField(max_length=500, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Symptom)


class Diagnosis(models.Model):
    symptoms = models.ForeignKey(Symptom, related_name="diagnosis", on_delete=models.CASCADE)
    result = models.TextField()
    slug =  models.SlugField(max_length=500, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.result
    
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_for_diagnosis(instance)

pre_save.connect(slug_generator, sender=Diagnosis)