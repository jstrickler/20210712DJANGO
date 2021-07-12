from django.shortcuts import render, HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("Welcome, to my groovy web app")

def cheese(request):
    return HttpResponse("Stinking Bishop")




