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
#run as manage.py test accounts.tests.tests_models.UserModelTestCase.userRegisterChecks
from django.test import TestCase
from accounts.models import User, Profile

#run as manage.py test accounts.tests.test_models.UserModelTestCase.userRegisterChecks
class UserModelTestCase(TestCase):
    @classmethod
    def setUp(self):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        user = User.objects.create(email='a@a.com',password='aa1234560')
        Profile.objects.create(user=user)

    def userRegisterChecks(self):
        print("Method: userRegisterChecks.")
        a_username = User.objects.get(username="aacom")
        self.assertEquals(str(a_username), 'aacom')

# run as manage.py test accounts.tests.test_models.ProfileModelTestCase.userProfileChecks
class ProfileModelTestCase(TestCase):
    @classmethod
    def setUp(self):
        user = User.objects.create(email='a@a.com',password='aa1234560')
        Profile.objects.create(user=user)
        
    def userProfileChecks(self):
        print("Method: userProfileChecks.")
        user = User.objects.get(id=1)
        a_profileRole = Profile.objects.get(user=user)
        self.assertEquals(str(a_profileRole.role), 'NURSE')

# get all tests: manage.py test --pattern=="tests*.py"

