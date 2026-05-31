from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('add/', views.add_patient, name='add_patient'),
    path('update/<int:pk>/', views.update_patient, name='update_patient'),
    path('delete/<int:pk>/', views.delete_patient, name='delete_patient'),
]