
from django.shortcuts import render, get_object_or_404
from .models import Wish
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WishSerializer
#import django class base views, import detail view
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
#add mixin to prevent creation of wish if your are not logged in
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class WishListView(ListView):
    model = Wish
    template_name = 'wishlist/LandingPage.html'
    #set wish variable to list objects
    context_object_name = 'posts'
    #order list from older to newest
    ordering = ['-date_posted']
    paginate_by = 4

class UserWishListView(ListView):
    model = Wish
    template_name = 'wishlist/user_wishes.html'
    #set wish variable to list objects
    context_object_name = 'posts'
    #order list from older to newest
    ordering = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Wish.objects.filter(author=user).order_by('-date_posted')


class WishDetailView(DetailView):
    model = Wish

class WishCreateView(LoginRequiredMixin, CreateView):
    model = Wish
    fields = ['title', 'content']

    #form valid method overwrite
    def form_valid(self, form):
        #set author to current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)
#add mixing to update your wish and not other peoples wishes
class WishUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Wish
    fields = ['title', 'content']

    #form valid method overwrite
    def form_valid(self, form):
        #set author to current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

    #check if current user is author of wish
    def test_func(self):
        wishlist = self.get_object()
        if self.request.user == wishlist.author:
            return True
        return False

#inherit mixins to make sure deleted wish is made by author and is signed in
class WishDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Wish
    #if delete is successful we redirect user to main page
    success_url = '/'

    #check if current user is author of wish
    def test_func(self):
        wishlist = self.get_object()
        if self.request.user == wishlist.author:
            return True
        return False


def about(request):
    return render(request, 'wishlist/about.html', {'title': 'About'})


#wishs/
class wishapi(APIView):
    
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id', -1)
        print(id)

        if id <= -1:
            wishes = Wish.objects.all()
            serializer = WishSerializer(wishes, many =True)
            print('if')
        else:
            try:
                wishes = Wish.objects.get(id=id)
            except Wish.DoesNotExist:
                # We have no object! Do something...
                pass
            
            serializer = WishSerializer(wishes, many =False)
            print('else')
        
        
        return Response(serializer.data)

    def post(self,request,format= None):
        data = request.data
        print(data)


        if(data['content'] == ''):
            serializer = WishSerializer(data=data,fields=('id','title','date_posted','author'))
        elif(data['date_posted'] == ''):
            serializer = WishSerializer(data=data,fields=('id','title','content','author'))
        elif(data['author'] == ''):
            serializer = WishSerializer(data=data,fields=('id','title','content','date_posted'))
        elif(data['author'] == '' and data['date_posted'] == ''):
            serializer = WishSerializer(data=data,fields=('id','title','content'))
        elif(data['author'] == '' and data['content'] == ''):
            serializer = WishSerializer(data=data,fields=('id','title','date_posted'))
        elif(data['content'] == '' and data['date_posted'] == ''):
            serializer = WishSerializer(data=data,fields=('id','title','author'))
        elif(data['content'] == '' and data['date_posted'] == '' and data['author'] == ''):
            serializer = WishSerializer(data=data,fields=('id','title'))
        else:
            serializer = WishSerializer(data=data,fields=('id','title','content','date_posted','author'))
            
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id', -1)
       
        wi = Wish.objects.get(id=id)
        wi.delete()
        res = {'msg':'Wish Deleted Successfully!'}
        return Response(res)
    
    
    
    
    


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

