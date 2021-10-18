from django.shortcuts import render
from .models import Wish, Users
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

# def createAccount(request):
#     if request.method == 'POST':
#         if request.POST.get('username') and request.POST.get('password'):
#             user = Users()
#             user.username = request.POST.get('username')
#
#             user.password = request.POST.get('password')
#             user.save()
#
#             return render(request, 'wishlist/login.html', {'title' : 'Login'})
#     else:
#         return render(request, 'wishlist/createaccount.html', {'title' : 'Create Account'})
#

# def products(request):
#     return HttpResponse('products')
#
# def customer(request):
#     return HttpResponse('customer')
#
# def create(request):
#     return render(request, 'createAccount.html')

