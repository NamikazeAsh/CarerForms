from django import forms

class DoctorForm(forms.Form):
    name = forms.CharField(max_length=100)
    speciality = forms.CharField(max_length=100)
    sub_speciality = forms.CharField(max_length=100)
    qualification = forms.CharField(widget=forms.Textarea)
    experience = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea)
    availability = forms.CharField(max_length=100)
    additional_details = forms.CharField(widget=forms.Textarea)