# products/urls.py
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),  # List of products
    path('create/', views.create_product, name='create_product'),  # Create product page
]
