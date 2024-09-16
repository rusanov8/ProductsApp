from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from .serializers import ProductSerializer


class ProductsListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

