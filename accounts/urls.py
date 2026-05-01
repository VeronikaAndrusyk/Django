from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
from django.urls import path
from doctors.views import doctor_list, doctor_create

urlpatterns = [
    path('', doctor_list, name='doctor_list'),
    path('create/', doctor_create, name='doctor_create'),
]