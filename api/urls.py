from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductsListCreateView.as_view(), name="api_products"),
]
