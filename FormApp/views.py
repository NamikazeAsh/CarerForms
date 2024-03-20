from django.shortcuts import render, redirect, get_object_or_404
from .forms import DoctorForm
from .models import Doctor
import uuid

def generate_form_link(request):
    form_slug = str(uuid.uuid4())[:8]  # Generate a unique slug for the form
    
    return redirect('open_form', form_slug=form_slug)

def open_form(request, form_slug):
    try:
        doctor = get_object_or_404(Doctor, slug=form_slug)
        form = DoctorForm(instance=doctor)
    except:
        form = DoctorForm()
    return render(request, 'carerForm.html', {'form': form, 'form_slug': form_slug})

def submit_form(request,form_slug):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('confirm_form', form_slug=form_slug)
    else:
        form = DoctorForm()
    return render(request, 'carerForm.html', {'form': form})

def confirm_form(request, form_slug):
    # Implement OTP confirmation logic here
    return render(request, 'confirmation.html')