from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Order
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import OrderSerializer, UserSerializer, GroupSerializer

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('product')
    serializer_class = OrderSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]