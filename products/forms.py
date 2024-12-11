# products/forms.py
from django import forms
from .models import Product
from .models import Transaction


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_photo', 'product_type', 'product_price', 'product_weight']


class BuyProductForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['quantity', 'payment_method']