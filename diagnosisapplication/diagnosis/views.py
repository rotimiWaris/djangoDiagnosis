from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import forms
from .models import Diagnosis, Symptom
from .serializers import SymptomSerializer, DiagnosisSerializer

# Create your views here.
def symptoms_list(request):
    symptoms = Symptom.objects.all().order_by('-date')
    return render(request, 'diagnosis/sypmtoms_list.html', { 'symptoms': symptoms })

def symptom_page(request, slug):
    symptom = Symptom.objects.get(slug=slug)
    return render(request, 'diagnosis/sypmtom_page.html', { 'symptom': symptom })

@login_required(login_url="/users/login/")
def create_symptom(request):
    if request.method == "POST":
        form = forms.CreateSymptom(request.POST)
        if form.is_valid():
            newsymptom = form.save(commit=False)
            newsymptom.author = request.user
            newsymptom.save()
            return redirect('diagnosis:symptom-list')
    else:
        form = forms.CreateSymptom()
    return render(request, 'diagnosis/create_symptom.html', { 'form': form })

def diagnosis_list(request):
    diagnoses = Diagnosis.objects.all().order_by('-date')
    return render(request, 'diagnosis/diagnosis_list.html', { 'diagnoses': diagnoses })

def diagnosis_page(request, slug):
    diagnosis = Diagnosis.objects.get(slug=slug)
    return render(request, 'diagnosis/diagnosis_page.html', { 'diagnosis': diagnosis })

@login_required(login_url="/users/login/")
def create_diagnosis(request):
    if request.method == "POST":
        form = forms.CreateDiagnosis(request.POST)
        if form.is_valid():
            newdiagnosis = form.save(commit=False)
            newdiagnosis.author = request.user
            newdiagnosis.save()
            return redirect('diagnosis:diagnosis-list')
    else:
        form = forms.CreateDiagnosis()
    return render(request, 'diagnosis/create_diagnosis.html', { 'form': form })

@login_required(login_url="/users/login/")
def symptom_history(request):
    symptoms = Symptom.objects.filter(author=request.user)
    return render(request, 'diagnosis/symptom_history.html', {'symptoms': symptoms})

@login_required(login_url="/users/login/")
def diagnosis_history(request):
    diagnoses = Diagnosis.objects.filter(author=request.user)
    return render(request, 'diagnosis/diagnosis_history.html', {'diagnoses': diagnoses})


@login_required
def update_symptom(request, symptom_id):
    symptom = get_object_or_404(Symptom, id=symptom_id, author=request.user)
    if request.method == 'POST':
        form = forms.UpdateSymptom(request.POST, instance=symptom)
        if form.is_valid():
            form.save()
            return redirect('diagnosis:symptom_history')
    else:
        form = forms.UpdateSymptom(instance=symptom)
    return render(request, 'diagnosis/update_symptom.html', {'form': form})

@login_required
def delete_symptom(request, symptom_id):
    symptom = get_object_or_404(Symptom, id=symptom_id, author=request.user)
    if request.method == 'POST':
        symptom.delete()
        return redirect('diagnosis:symptom_history')
    return render(request, 'diagnosis/confirm_delete.html', {'symptom': symptom})

@login_required
def update_diagnosis(request, diagnosis_id):
    diagnosis = get_object_or_404(Diagnosis, id=diagnosis_id, author=request.user)
    if request.method == 'POST':
        form = forms.UpdateDiagnosis(request.POST, instance=diagnosis)
        if form.is_valid():
            form.save()
            return redirect('diagnosis:diagnosis_history')
    else:
        form = forms.UpdateDiagnosis(instance=diagnosis)
    return render(request, 'diagnosis/update_diagnosis.html', {'form': form})

@login_required
def delete_diagnosis(request, diagnosis_id):
    diagnosis = get_object_or_404(Diagnosis, id=diagnosis_id, author=request.user)
    if request.method == 'POST':
        diagnosis.delete()
        return redirect('diagnosis:diagnosis_history')
    return render(request, 'diagnosis/confirm_delete.html', {'diagnosis': diagnosis})


# API
class SymptomListCreate(generics.ListCreateAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

    def delete(self, request, *args, **kwargs):
        Symptom.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SymptomRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    lookup_field = 'pk'

class DiagnosisListCreate(generics.ListCreateAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer

    def delete(self, request, *args, **kwargs):
        Diagnosis.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DiagnosisRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
    lookup_field = 'pk'