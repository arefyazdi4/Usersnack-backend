from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action, permission_classes
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from .models import Customer, Order, OrderItem, Product, Pizza, Incredient
from .serializers import CustomerSerializer, PizzaSerializer


class PizzaViewSet(ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]


# class OrderViewSet(ModelViewSet):
#     http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']
#
#     def create(self, request, *args, **kwargs):
#         serializer = CreateOrderSerializer(
#             data=request.data,
#             context={'user_id': self.request.user.id})
#         serializer.is_valid(raise_exception=True)
#         order = serializer.save()
#         serializer = OrderSerializer(order)
#         return Response(serializer.data)
#
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return CreateOrderSerializer
#         return OrderSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         (customer, created) = Customer.objects.get_or_create(user_id=request.user.id)
#         customer_id = Customer.objects.only(
#             'id').get(user_id=user.id)
#         return Order.objects.filter(customer_id=customer_id)
