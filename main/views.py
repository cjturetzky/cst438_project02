from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'LandingPage.html')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')


# def products(request):
#     return HttpResponse('products')
#
# def customer(request):
#     return HttpResponse('customer')
#
# def create(request):
#     return render(request, 'createAccount.html')

