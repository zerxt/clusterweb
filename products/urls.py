# products/urls.py
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),  # List of products
    path('create/', views.create_product, name='create_product'),  # Create product page
    path('<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('my_products/', views.my_products, name='my_products'),
]
