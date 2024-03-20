from django.shortcuts import render, redirect, get_object_or_404
from .forms import DoctorForm
from .models import Doctor
import uuid
from django.utils.text import slugify

def generate_form_link(request):
    form_slug = str(uuid.uuid4())[:8]
    
    return redirect('open_form', form_slug=form_slug)

def open_form(request, form_slug):
    try:
        doctor = get_object_or_404(Doctor, slug=form_slug)
        form = DoctorForm(request.POST or None, instance=doctor)
    except:
        form = DoctorForm()
    
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.instance.slug = slugify(form_slug)
            form.save()
            return redirect('open_form', form_slug=form_slug)
    
    return render(request, 'carerForm.html', {'form': form, 'form_slug': form_slug})

def submit_form(request,form_slug):
    if request.method == 'POST':
        print("ITS ATLEAST POSTING")
        form = DoctorForm(request.POST)
        print(form.data)
        if form.is_valid():
            print("Valid!!!!!!!!!!!!!!!!!!!!!!!")
            form.save()  # Save the form data to the database
            return redirect('open_form', form_slug=form_slug)
    else:
        print("-------FORM INIT--------")
        form = DoctorForm()
    return render(request, 'carerForm.html', {'form': form})

def confirm_form(request, form_slug):
    # Implement OTP confirmation logic here
    return render(request, 'confirmation.html')