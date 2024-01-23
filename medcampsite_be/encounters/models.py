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
# class Encounter(models.Model):

#     patient = models.CharField(max_length=255)
#     encounter_date = models.DateTimeField(auto_now_add=True)
#     presenting_complaint = models.CharField(max_length=255)
#     pt_photo = models.ImageField(upload_to='patients/%Y/%m/%d/',blank=True)

#     class Meta:
#         ordering = ['id']
#         indexes = [ models.Index(fields=['pt_surname'])]

#     def __str__(self):
#         return f'Patient {self.pt_surname} {self.pt_firstname}'
