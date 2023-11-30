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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from django.contrib.auth import views as auth_views

schema_view = get_schema_view(
   openapi.Info(
      title="Medical Camp System API",
      default_version='v1',
      description="Official Backend API of the Medical camp system" 
                    +"\n Django v4.2 : https://docs.djangoproject.com/en/4.2/"
                    +"\n Rest Freamework : v3.14 https://www.django-rest-framework.org/",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="akiyofidel@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)



urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/web/', include('accounts.urls')),
    path('api/v1/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/mob/auth/', include('rest_registration.api.urls')),
    #path('api/v2/auth/', include('django.contrib.auth.urls')),
    # path('api/v3/auth/', include('dj_rest_auth.urls')),
    # path('api/v4/auth/', include('rest_email_auth.urls'))


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)