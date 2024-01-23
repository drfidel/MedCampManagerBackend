"""
    Copyright (C) <2023>  <Dr. Akiyo Fidel>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>


"""
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
    
class Patient(models.Model):
    
    class Gender(models.TextChoices):
        MALE = 'M','Male'
        FEMALE = 'F','Female'
    
    class Profession(models.TextChoices):
        DOCTOR = 'DR', 'Doctor'
        ENGINEER = 'ENG','Engineer'
        PEASANT = 'PES','Peasant'
        STUDENT = 'STU','Student'

    pt_salutation = models.CharField(max_length=255)
    pt_firstname = models.CharField(max_length=255)
    pt_surname = models.CharField(max_length=255)
    pt_gender = models.CharField(max_length=2,choices=Gender.choices, default=Gender.FEMALE)
    pt_age = models.CharField(max_length=255)
    pt_profession = models.CharField(max_length=3,choices=Profession.choices, default=Profession.PEASANT)
    pt_contact = models.CharField(max_length=255)
    pt_religion = models.CharField(max_length=255)
    pt_village = models.CharField(max_length=255)
    pt_parish = models.CharField(max_length=255)
    pt_subcounty = models.CharField(max_length=255)
    pt_district = models.CharField(max_length=255)
    pt_nationality = models.CharField(max_length=255)
    pt_nin = models.CharField(max_length=255)
    pt_photo = models.ImageField(upload_to='patients/%Y/%m/%d/',blank=True)
    visit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        indexes = [ models.Index(fields=['pt_surname'])]

    def __str__(self):
        return f'{self.pt_surname} {self.pt_firstname}'

class Encounter(models.Model):
    identity = models.ForeignKey('Patient', related_name='patient', on_delete=models.CASCADE)
    presenting_complaint = models.CharField(max_length=255, blank=True, null=True)
    diagnosis = models.CharField(max_length=255, blank=True, null=True)
    prescription = models.CharField(max_length=255, blank=True, null=True)
    labrequest = models.CharField(max_length=255, blank=True, null=True)
    visit_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['id']
        indexes = [ models.Index(fields=['identity'])]
    

    def __str__(self):
        return f'{self.identity}'
    
    def __int__(self):
        return self.identity

class Labtest(models.Model):
    identitylab = models.ForeignKey(Patient, related_name='patientid', on_delete=models.CASCADE)
    encounterid = models.ForeignKey(Encounter, on_delete=models.CASCADE)
    presenting_complaint = models.CharField(max_length=255, blank=True, null=True)
    diagnosis = models.CharField(max_length=255, blank=True, null=True)
    labrequest = models.CharField(max_length=255, blank=True, null=True)
    sampletaken = models.CharField(max_length=255, blank=True, null=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    conclusion = models.CharField(max_length=255, blank=True, null=True)
    requestingdoctor =models.CharField(max_length=255, blank=True, null=True)
    visit_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['id']
        indexes = [ models.Index(fields=['identitylab'])]
    

    def __str__(self):
        return f'{self.identitylab}'
    
    def __int__(self):
        return f'{self.identitylab}'

    def __unicode__(self):
        return self.identitylab