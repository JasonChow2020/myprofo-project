from django.shortcuts import render

from .models import Job #import class named Job from models.py

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs}) #jobs is reference for html
