from django.urls import path
from .views import home_view, customer_view, product_view, order_view
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProductViewSet, OrderViewSet

urlpatterns = [
    path('', home_view, name='home'),
    path('customers', customer_view, name='customer'),
    path('products', product_view, name='product'),
    path('orders', order_view, name='order'),
]


router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls