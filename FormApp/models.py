from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    sub_speciality = models.CharField(max_length=100)
    qualification = models.TextField()
    experience = models.CharField(max_length=100)
    address = models.TextField()
    availability = models.CharField(max_length=100)
    additional_details = models.TextField()
    slug = models.SlugField(unique=True)