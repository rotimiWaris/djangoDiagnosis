from django.urls import path
from . import views

app_name = 'diagnosis'

urlpatterns = [
    path('', views.diagnosis_list, name="diagnosis-list"),
    path('symp/', views.symptoms_list, name="symptom-list"),
    path('new-diagnosis/', views.create_diagnosis, name="create-diagnosis"),
    path('new-symptom/', views.create_symptom, name="create-symptom"),
    path('symptom-history/', views.symptom_history, name='symptom_history'),
    path('diagnosis-history/', views.diagnosis_history, name='diagnosis_history'),
    path('update/symp/<int:symptom_id>/', views.update_symptom, name='update_symptom'),
    path('delete/symp/<int:symptom_id>/', views.delete_symptom, name='delete_symptom'),
    path('update/<int:diagnosis_id>/', views.update_diagnosis, name='update_diagnosis'),
    path('delete/<int:diagnosis_id>/', views.delete_diagnosis, name='delete_diagnosis'),
    path('symp/<slug:slug>', views.symptom_page, name="symptom-page"),
    path('<slug:slug>', views.diagnosis_page, name="diagnosis-page"),

    # API
    path('api/symp/', views.SymptomListCreate.as_view(), name="symptom-view-create"),
    path('api/symp/<int:pk>/', views.SymptomRetrieveUpdateDestroy.as_view(), name="symptom-update"),
    path('api/diagnosis/', views.DiagnosisListCreate.as_view(), name="diagnosis-view-create"),
    path('api/diagnosis/<int:pk>/', views.DiagnosisRetrieveUpdateDestroy.as_view(), name="diagnosis-update"),
]
