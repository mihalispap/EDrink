"""EDrink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from edrink import views
from edrink.forms import CustomRegistration, SignUpForm

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/register/',
         CustomRegistration.as_view(success_url='/admin/', form_class=SignUpForm),
         name='django_registration_register'),
    url(r'^admin/profile/edit/$', views.edit_profile, name='edit_profile'),
]
