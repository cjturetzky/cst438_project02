from django.shortcuts import render
from django.http import HttpResponse

# create your views here
import cst438_project02


def home(request):
    return render(request, 'static/LandingPage.html')

def products(request):
    return HttpResponse('products')

def customer(request):
    return HttpResponse('customer')