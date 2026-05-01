from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Doctor
from .forms import DoctorForm

def is_doctor(user):
    return user.groups.filter(name='Doctor').exists()

def is_admin(user):
    return user.groups.filter(name='Admin').exists()


def is_doctor_or_admin(user):
    return (
        user.groups.filter(name='Doctor').exists()
        or user.groups.filter(name='Admin').exists()
    )




def doctor_list(request):
    specialization = request.GET.get('specialization')

    
    if not specialization:
        specialization = request.COOKIES.get('favorite_spec')

    doctors = Doctor.objects.all()

    if specialization:
        doctors = doctors.filter(specialization=specialization)

    response = render(request, 'doctors/doctor_list.html', {
        'doctors': doctors,
        'current_spec': specialization
    })

  
    if request.GET.get('specialization'):
        response.set_cookie(
            'favorite_spec',
            specialization,
            max_age=60 * 60 * 24  
        )

    return response



@user_passes_test(is_admin)
def doctor_create(request):
    form = DoctorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('doctor_list')

    return render(request, 'doctors/doctor_form.html', {'form': form})


@user_passes_test(is_doctor_or_admin)
def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)

    form = DoctorForm(request.POST or None, instance=doctor)

    if form.is_valid():
        form.save()
        return redirect('doctor_list')

    return render(request, 'doctors/doctor_form.html', {'form': form})




def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)

    request.session['last_doctor_id'] = doctor.id

    return render(request, 'doctors/doctor_detail.html', {
        'doctor': doctor
    })




def last_viewed_doctor(request):
    doctor_id = request.session.get('last_doctor_id')
    doctor = None

    if doctor_id:
        doctor = Doctor.objects.filter(id=doctor_id).first()

    return render(request, 'doctors/last_viewed.html', {
        'doctor': doctor
    })

def doctors_list(request):
    specialty = request.GET.get('specialty')

    # якщо GET нема — беремо cookie
    if not specialty:
        specialty = request.COOKIES.get('specialty_filter')

    doctors = Doctor.objects.all()

    if specialty:
        doctors = doctors.filter(specialization=specialty)

    response = render(request, 'doctors/doctor_list.html', {
        'doctors': doctors,
        'current_spec': specialty
    })

    # якщо користувач вибрав фільтр — зберігаємо cookie
    if request.GET.get('specialty'):
        response.set_cookie('specialty_filter', specialty, max_age=86400)

    return response