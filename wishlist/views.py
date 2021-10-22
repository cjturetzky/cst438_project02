from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WishSerializer
#
from django.shortcuts import render
from .models import Wish, WishlistItem
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

def listview(request):
    posts = WishlistItem.objects.all()
    return render(request, 'wishlist/listview.html',{'posts':posts})

#wishs/
class wishapi(APIView):

    def get(self,request):
        wishes = Wish.objects.all()
        serializer = WishSerializer(wishes, many =True)
        return Response(serializer.data)

    def post(self):
        pass
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

