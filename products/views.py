from django.shortcuts import get_object_or_404
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

@login_required
def my_products(request):
    try:
        resident = Resident.objects.get(user=request.user)  # Get the resident associated with the user
        products = Product.objects.filter(added_by=resident)  # Fetch products added by this resident
    except Resident.DoesNotExist:
        products = []  # If no resident is found, show an empty list

    return render(request, 'products/my_products.html', {'products': products})

@login_required
def edit_product(request, product_id):
    try:
        resident = Resident.objects.get(user=request.user)  # Get the logged-in user's resident profile
    except Resident.DoesNotExist:
        messages.error(request, "You are not associated with a resident account.")
        return redirect('products:product_list')

    # Ensure the resident can only edit their own product
    product = get_object_or_404(Product, id=product_id, added_by=resident)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('products:product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/edit_product.html', {'form': form, 'product': product})


@login_required
def delete_product(request, product_id):
    # Get the product to delete or return 404 if not found
    product = get_object_or_404(Product, id=product_id)
    
    # Get the current resident
    resident = Resident.objects.get(user=request.user)
    
    # Check if the product belongs to the logged-in resident
    if product.added_by != resident:
        return HttpResponseForbidden("You are not allowed to delete this product.")
    
    # Delete the product
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect('products:my_products')  # Redirect to the user's products page

# products/views.py
def product_chat(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/product_chat.html', {
        'product': product
    })
