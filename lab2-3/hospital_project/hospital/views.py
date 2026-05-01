from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Doctor, Appointment


def appointment_list(request):
    diagnosis = request.GET.get('diagnosis')

    appointments = Appointment.objects.all()

    if diagnosis:
        appointments = appointments.filter(diagnosis__icontains=diagnosis)

    return render(request, 'hospital/appointment_list.html', {
        'appointments': appointments
    })


def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    return render(request, 'hospital/appointment_detail.html', {
        'appointment': appointment
    })


def doctor_list(request):
    doctors = Doctor.objects.all()

    return render(request, 'hospital/doctor_list.html', {
        'doctors': doctors
    })