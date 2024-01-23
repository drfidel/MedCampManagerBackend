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
from django.urls import path, include
from .views import PatientListView, SinglePatientView, EncounterListView, SingleEncounterView, LabtestListView, SingleLabtestView

urlpatterns = [
    path('patient', PatientListView.as_view()),
    path('patient/<int:pk>', SinglePatientView.as_view()),
    path('encounter', EncounterListView.as_view()),
    path('encounter/<int:pk>', SingleEncounterView.as_view()),
    path('labtest', LabtestListView.as_view()),
    path('labtest/<int:pk>', SingleLabtestView.as_view()),
]
