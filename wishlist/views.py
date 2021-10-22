
from django.shortcuts import render, get_object_or_404
from .models import Wish
from django.contrib.auth.models import User
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



# def products(request):
#     return HttpResponse('products')
#
# def customer(request):
#     return HttpResponse('customer')
#
# def create(request):
#     return render(request, 'createAccount.html')

