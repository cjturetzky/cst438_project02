from django.shortcuts import render
from .models import Wish
# Create your views here.

posts = [
    {
        'author': 'Ramiro',
        'title': 'post 1',
        'content': 'first content',
        'date': 'cot 10, 2021'
    },
    {
        'author': 'Leo',
        'title': 'part 2',
        'content': 'second content',
        'date': 'cot 11, 2021'

    }
]

def home(request):
    context = {
        'posts': Wish.objects.all()
    }
    return render(request, 'wishlist/LandingPage.html', context)

def about(request):
    return render(request, 'wishlist/about.html', {'title': 'About'})


# def products(request):
#     return HttpResponse('products')
#
# def customer(request):
#     return HttpResponse('customer')
#
def listView(request):
    return render(request, 'wishlist/listView.html')

def register(request):
    return render(request, 'wishlist/register.html')

