from django import forms
from .models import *

class DoctorForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    speciality = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sub_speciality = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    qualification = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    experience = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    availability = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    additional_details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))