from django.shortcuts import render
from .models import Wish
#import django class base views, import detail view
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
#add mixin to prevent creation of wish if your are not logged in
from django.contrib.auth.mixins import LoginRequiredMixin

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

