""" contacts project URL Configuration
    The urlpatterns list routes URLs to views. 
"""

from django.contrib import admin
from django.urls import path 
from contactslist import views
urlpatterns = [ 

    path('display/',views.display),
    path('contactslist/',views.index),
    path('admin/', admin.site.urls),]