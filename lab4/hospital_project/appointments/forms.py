from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient_name', 'date', 'reason']

    def clean_patient_name(self):
        name = self.cleaned_data['patient_name']
        if len(name) < 3:
            raise forms.ValidationError("Ім'я занадто коротке")
        return name