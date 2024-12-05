from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from residents.models import Resident

def product_list(request):
    # Fetch all products from the database
    products = Product.objects.all()

    # Pass the products to the template
    return render(request, 'products/product_list.html', {'products': products})

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)  # Don't save yet, to attach the resident
            product.added_by = Resident.objects.get(user=request.user)  # Attach the current resident
            product.save()
            messages.success(request, "Product added successfully!")
            return redirect('products:product_list')
    else:
        form = ProductForm()
    
    return render(request, 'products/create_product.html', {'form': form})