from django.shortcuts import render
from django.http import HttpResponse

# create your views here

def home(request):
    return HttpResponse('Home')

def products(request):
    return HttpResponse('products')

def customer(request):
    return HttpResponse('customer')