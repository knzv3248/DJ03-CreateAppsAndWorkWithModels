from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "MyDjango/index.html")

def new(request):
    return render(request, "MyDjango/new.html")

def my_tests(request):
    return render(request, "MyDjango/tests.html")

def my_data(request):
    return render(request, "MyDjango/data.html")
