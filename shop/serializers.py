from rest_framework import serializers
from .models import Customer, Product, Order


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model =Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'created_at']
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = ['product_name', 'price', 'quantity', 'description']
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =Order
        fields = ['customer', 'product', 'order_status', 'created_at', 'updated_at']