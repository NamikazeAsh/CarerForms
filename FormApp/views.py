from django.shortcuts import render, redirect, get_object_or_404
from .forms import DoctorForm
from .models import Doctor
import uuid
from django.utils.text import slugify
from django.db import IntegrityError



def generate_form_link(request):
    
    if request.method == 'POST':    
        form_slug = str(uuid.uuid4())[:8]
        return redirect('open_form', form_slug=form_slug)
    else:
        return render(request,"home.html")
    
def open_form(request, form_slug):
    try:
        doctor = get_object_or_404(Doctor, slug=form_slug)
        form = DoctorForm(request.POST or None, instance=doctor)
    except:
        form = DoctorForm()
    
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            try:
                form.instance.slug = slugify(form_slug)
                form.save()
            except IntegrityError:
                existing_doctor = Doctor.objects.get(slug=form_slug)
                form.instance.pk = existing_doctor.pk  # Update the existing instance
                form.save()
            return redirect('open_form', form_slug=form_slug)
    
    return render(request, 'carerForm.html', {'form': form, 'form_slug': form_slug})

def confirm_form(request, form_slug):
    # Implement OTP confirmation logic here
    return render(request, 'confirmation.html')


# Twilio OTP logic
# otp = str(random.randint(1000, 9999))
#                 client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#                 try:
#                     message = client.messages.create(body=f'Your OTP is: {otp}',from_=settings.TWILIO_PHONE_NUMBER,to="+91"+email)
#                     #Storing in session
#                     request.session['otp'] = otp
#                     request.session['email'] = email
#                     return JsonResponse({'success': True})
                
#                 except Exception as e:
#                     return JsonResponse({'success': False, 'error': str(e)})