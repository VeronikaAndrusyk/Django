from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('add/', views.appointment_create, name='appointment_add'),
    path('edit/<int:pk>/', views.appointment_edit, name='appointment_edit'),
]