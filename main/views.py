from django.shortcuts import render

# Create your views here.
def index(response, id):
    return HttpResponse("<h1>%s</h1>" %  id);