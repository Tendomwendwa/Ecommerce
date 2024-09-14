from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Product, Order
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer

# Create your views here.
def home_view(request):
    return render (request, 'shop/home.html')

def customer_view(request):
    return render (request, 'shop/customers.html')

def product_view(request):
    return render (request, 'shop/products.html')

def order_view(request):
    return render (request, 'shop/orders.html')


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer