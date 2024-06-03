from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
from django.templatetags.static import static
from django.urls import path

def home(request):
     
    return render(request , 'home.html')

def about(request):
     
    return render(request , 'about.html')

def slider(request):
     
    return render(request , 'slider.html')

def q1(request):
     
    return render(request , 'q1.html')
    
