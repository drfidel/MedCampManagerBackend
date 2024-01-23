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
from rest_framework import serializers
from patients.models import Patient, Encounter, Labtest
from rest_framework.response import Response
from django.core import exceptions

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class EncounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encounter
        fields = '__all__'

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labtest
        fields = '__all__'
