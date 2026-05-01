from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialty', 'phone']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) < 10:
            raise forms.ValidationError("Телефон має бути мінімум 10 символів")
        return phone