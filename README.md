# MedCampManagerBackend

MediCampManagerBack end is a standalone Backend service that shall handle and store user and customer data for the Medical Camp manager Application.

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](code_of_conduct.md)

## About

The purpose of this project is to help digitise medical camps to enable their activity as an adjunct to the medical service delivery. Its targets are [is] to span a variety of challenges related to preparation and successful execution of medical camps and provide the necessary data required for research and planning at the MoH levels.

This project addresses the following SDG targets:

- reduce the global maternal mortality ratio to less than 70 per 100,000 live births

- end preventable deaths of newborns and children under 5 years of age, with all countries aiming to reduce neonatal mortality to at least as low as 12 per 1,000 live births and under-5 mortality to at least as low as 25 per 1,000 live births

- By 2030, end the epidemics of AIDS, tuberculosis, malaria and neglected tropical diseases and combat hepatitis, water-borne diseases and other communicable diseases

- reduce by one third premature mortality from non-communicable diseases through prevention and treatment and promote mental health and well-being

- Strengthen the prevention and treatment of substance abuse, including narcotic drug abuse and harmful use of alcohol

- ensure universal access to sexual and reproductive health-care services, including for family planning, information and education, and the integration of reproductive health into national strategies and programmes

- Achieve universal health coverage, including financial risk protection, access to quality essential health-care services and access to safe, effective, quality and affordable essential medicines and vaccines for all

- Substantially increase health financing and the recruitment, development, training and retention of the health workforce in developing countries, especially in least developed countries and small island developing States

## Why

Talk about what problem this solves, what SDG(s) and SGD targets it addresses and why these are important

## Usage

How would someone use what you have built, include URLs to the deployed app, service e.t.c when you have it setup

## Setup

- Clone this repository by running `git clone`

- create Virtual developer project environment
`virtualenv venv`

`python3 -m venv venv`

- open virtualenvironment
In windows
`venv\scripts\activate`

- In Linux
`source venv/bin/activate`

- install dependencies in virtual dev environment
`pip install -r requirements.txt`

- update dependencies list
`pip freeze -> requirements.txt`

- run the developement server
`cd medcampsite_be`
`python manage.py runserver`

`python manage.py makemigrations --settings=medcampsite_be.settings.local`
`python manage.py migrate --settings=medcampsite_be.settings.local`
`python manage.py createsuperuser --settings=medcampsite_be.settings.local`
`python manage.py runserver --settings=medcampsite_be.settings.local`

- Navigate to `http://localhost:8000/api/v1/index` to view the running application and get started

## Deployment

- This application can also be accessed at `https://"".herokuapp.com/`
- To test out as administrator login with these credentials

## API Usage

### WEB AUTHENTICATION

| REQUEST | ROUTE                                       | FUNCTIONALITY                                  |
| ------- | ------------------------------------------- | ---------------------------------------------- |
| POST    | api/v1/web/auth/login/                      | Logs in a user                                 |
| POST    | api/v1/web/auth/register/                   | Registers a user                               |
| POST    | api/v1/web/auth/logout/                     | Logs out a user                                |
| POST    | api/v1/web/auth/password/reset/             | sends password reset link                      |
| POST    | api/v1/web/auth/password/reset/confirm/     | confirms password reset and sets new password  |
| POST    | api/v1/web/auth/password/change/            | changes logged in account password             |

### MOBILE AUTHENTICATION

| REQUEST | ROUTE                                       | FUNCTIONALITY                                 |
| ------- | ----------------------------------------    | ----------------------------------------------|
| POST    | api/v1/mob/auth/login/                      | Logs in a user                                |
| POST    | api/v1/mob/auth/signup/                     | Registers a user                              |
| POST    | api/v1/mob/auth/logout/                     | Logsout a user                                |
| POST    | api/v1/mob/auth/verify-email/               | verifies email                                |
| POST    | api/v1/mob/auth/resend-email/               | resend verify email                           |
| POST    | api/v1/mob/auth/password/reset/             | sends password reset link                     |
| POST    | api/v1/mob/auth/password/reset/confirm/     | confirms password reset and sets new password |
| POST    | api/v1/mob/auth/password/change/            | changes logged in account password            |

### PATIENTS

| REQUEST | ROUTE                        | FUNCTIONALITY                             |
| ------- | ---------------------------- | ----------------------------------------- |
| GET     | api/v1/patients              | Fetches all patients                      |

### USERS

| REQUEST | ROUTE                               | FUNCTIONALITY            |
| ------- | ----------------------------        | ------------------------ |
| GET     | api/v1/web/auth/profile/<int:pk>    | Fetches user profile     |
| PUT     | api/v1/web/auth/profile/<int:pk>    | Edits a user profile     |
| GET     | api/v1/web/auth/user/<int:pk>       | Fetches a users details  |
| PUT     | api/v1/web/auth/user/<int:pk>       | Edits a users details    |
| GET     | api/v1/mob/auth/user/               | Fetches a users details  |
| PUT     | api/v1/mob/auth/user/               | Edits a users details  |

### SWAGGER API DOCUMENTATION

| REQUEST | ROUTE                        | FUNCTIONALITY            |
| ------- | ---------------------------- | ------------------------ |
| GET     | api/v1/swagger/      | Fetches API documentation summary view          |
| PUT     | api/v1/redoc/                | Details of API                     |

### ADMIN SITE

| REQUEST | ROUTE                        | FUNCTIONALITY            |
| ------- | ---------------------------- | ------------------------ |
| GET     | api/v1/admin/                | Login to admin site      |

## Postman Setup for API Testing

Open this collection in postman by clicking the button below:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/6812201-86e0b5ca-2b9e-4a1c-a4f0-ab7fa633d063?action=collection%2Ffork&collection-url=entityId%3D6812201-86e0b5ca-2b9e-4a1c-a4f0-ab7fa633d063%26entityType%3Dcollection%26workspaceId%3Dc8cce30c-57cd-42ec-8792-3247f1262b77)

If you're using Postman for testing the REST api, you can use the following setup:

### TESTING AUTHENTICATION BACKEND

- Make sure you have an environment set for your collection.

- POST to `http://localhost:8000/api/v1/web/auth/signup/` and add your details to sign up on WEB

- POST to `http://localhost:8000/api/v1/mob/auth/signup/` and add your details to sign up on MOBILE

- POST to `http://localhost:8000/api/v1/web/auth/login/` to login and obtain token for WEB

- POST to `http://localhost:8000/api/v1/mob/auth/login/` to login and obtain token for MOBILE

- Paste this code in Tests which will save the token to the environment.

- In the Authorization section of your subsequent posts, set the CSRF Token given in login cookie on X-CSRFToken header
    for every Post request.

- POST to `http://localhost:8000/api/v1/web/auth/login/` to logout session for WEB

- POST to `http://localhost:8000/api/v1/mob/auth/login/` to logout session for MOBILE

## Authors

- [Akiyo Fidel](https://github.com/drfidel)

## LICENSE

GNU
