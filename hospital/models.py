from django.db import models


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date}"