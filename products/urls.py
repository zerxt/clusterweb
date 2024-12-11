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
    path('<int:product_id>/chat/', views.product_chat, name='product_chat'),  

    path('buy/<int:product_id>/', views.buy_product, name='buy_product'),
    path('list/', views.transaction_list, name='transaction_list'),

    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
]


