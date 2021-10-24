from django.contrib import admin
from django.urls import path, include
#from helpinghand.home.views import Maidservices
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('Maidservices', views.Maidservices, name='Maidservices')
]