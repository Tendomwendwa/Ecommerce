from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_view),
    path('customers', views.customer),
    path('products', views.product),
    path('orders', views.order),
]