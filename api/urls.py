from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('pizzas', views.PizzaViewSet, basename='pizzas')
router.register('customers', views.CustomerViewSet)
# router.register('orders', views.OrderViewSet, basename='orders')

urlpatterns = router.urls