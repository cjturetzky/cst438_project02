from django.shortcuts import render
from django.http import HttpResponse

# create your views here

def home(request):
    return render(request, 'static/LandingPage.html')

def products(request):
    return HttpResponse('products')

def customer(request):
    return HttpResponse('customer')

def create(request):
    return render(request, 'createAccount.html')

