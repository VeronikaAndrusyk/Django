from django.db import models

class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField(default=0) # Стаж замість телефону



    def __str__(self):
        return self.full_name
    