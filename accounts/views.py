from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,'Registration.html')

def log_gin(request):
    return render(request,'log.html')
