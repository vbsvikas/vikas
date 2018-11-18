from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'homepage.html')
#     return HttpResponse('homepage')

def about(request):
    return render(request,'about.html')
#    return HttpResponse('about')