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
from django.contrib import admin
from .models import Patient, Encounter, Labtest

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id','pt_surname','pt_firstname','pt_age','pt_gender','visit_date']

@admin.register(Encounter)
class EncounterAdmin(admin.ModelAdmin):
    list_display = ['id','visit_date','identity', 'labrequest','diagnosis', 'prescription']

@admin.register(Labtest)
class LabtestAdmin(admin.ModelAdmin):
    list_display = ['id','visit_date','identitylab', 'encounterid','labrequest', 'result', 'conclusion']
