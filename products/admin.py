from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_type', 'product_price', 'product_weight', 'date_added', 'added_by')
    search_fields = ('product_name', 'product_type', 'added_by__name')  # Assuming Resident has a 'name' field
    list_filter = ('product_type', 'date_added')

admin.site.register(Product, ProductAdmin)
