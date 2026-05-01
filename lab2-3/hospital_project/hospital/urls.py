from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('doctors/', views.doctor_list, name='doctor_list'),
]