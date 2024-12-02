from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages

def product_list(request):
    # Fetch all products from the database
    products = Product.objects.all()

    # Pass the products to the template
    return render(request, 'products/product_list.html', {'products': products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # include request.FILES to handle image uploads
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect('products:product_list')  # Redirect to the product list page after successful creation
    else:
        form = ProductForm()
    
    return render(request, 'products/create_product.html', {'form': form})