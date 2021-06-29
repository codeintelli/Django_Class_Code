from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.index ,name="index"),
    path('about', views.about ,name="index"),
    path('contact', views.contact ,name="index"),
    path('services', views.services ,name="index"),
]