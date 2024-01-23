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
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from patients.api.serializers import PatientSerializer, EncounterSerializer, LabSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import permissions
from accounts.models import User
from .models import Patient, Encounter, Labtest
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

class PatientListView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

class SinglePatientView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

class EncounterListView(ListCreateAPIView):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    permission_classes = [permissions.IsAuthenticated]

class SingleEncounterView(RetrieveUpdateDestroyAPIView):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    permission_classes = [permissions.IsAuthenticated]

class LabtestListView(ListCreateAPIView):
    queryset = Labtest.objects.all()
    serializer_class = LabSerializer
    permission_classes = [permissions.IsAuthenticated]

class SingleLabtestView(RetrieveUpdateDestroyAPIView):
    queryset = Labtest.objects.all()
    serializer_class = LabSerializer
    permission_classes = [permissions.IsAuthenticated]
