from django.db import models

# Create your models here.
from django.db import models
from doctors.models import Doctor

class Appointment(models.Model):
    patient_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    phone = models.CharField(max_length=20)
    complaints = models.TextField()
    appointment_date = models.DateTimeField()
    
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    diagnosis = models.CharField(max_length=255)
    treatment_description = models.TextField()

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date}"