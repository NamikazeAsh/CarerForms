from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    sub_speciality = models.CharField(max_length=100)
    qualification = models.CharField(max_length=500)
    experience = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    availability = models.CharField(max_length=100)
    additional_details = models.TextField(null=True,blank=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name