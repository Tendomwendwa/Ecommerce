from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse ('home')

def customer(request):
    return HttpResponse ('customers')

def product(request):
    return HttpResponse ('products')

def order(request):
    return HttpResponse ('orders')

