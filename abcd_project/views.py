from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def message(request):
    return render(request,'message.html')