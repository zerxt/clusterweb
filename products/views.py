from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProductForm, BuyProductForm
from .models import Transaction, Cart, CartItem, Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from residents.models import Resident


from django.shortcuts import render
from .models import Product

def product_list(request):
    search_query = request.GET.get('search', '')  # Get the search query from the GET request
    products = Product.objects.all()

    # Filter products based on the search query
    if search_query:
        products = products.filter(product_name__icontains=search_query)

    return render(request, 'products/product_list.html', {
        'products': products,
        'search_query': search_query  # Pass the search query to the template
    })

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
    
@login_required
def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    try:
        buyer = Resident.objects.get(user=request.user)
    except Resident.DoesNotExist:
        messages.error(request, "You need to be associated with a resident account to make a purchase.")
        return redirect('products:product_list')

    total_cost = 0
    if request.method == 'POST':
        form = BuyProductForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            total_cost = quantity * product.product_price
            payment_method = form.cleaned_data['payment_method']

            transaction = Transaction(
                buyer=buyer,
                seller=product.added_by,
                product=product,
                quantity=quantity,
                total_price=total_cost,
                payment_method=payment_method
            )
            transaction.save()

            messages.success(request, "Purchase successful!")
            return redirect('products:transaction_list')
    else:
        form = BuyProductForm()

    return render(request, 'products/buy_product.html', {
        'product': product,
        'form': form,
        'total_cost': total_cost  # Pass the calculated total cost to the template
    })

@login_required
def transaction_list(request):
    try:
        resident = Resident.objects.get(user=request.user)
    except Resident.DoesNotExist:
        messages.error(request, "You need to be associated with a resident account to view transactions.")
        return redirect('products:product_list')

    buyer_transactions = Transaction.objects.filter(buyer=resident).order_by('-transaction_date')
    seller_transactions = Transaction.objects.filter(seller=resident).order_by('-transaction_date')

    return render(request, 'products/transaction_list.html', {
        'buyer_transactions': buyer_transactions,
        'seller_transactions': seller_transactions
    })

@login_required
def cart_detail(request):
    try:
        cart = Cart.objects.get(resident__user=request.user)
    except Cart.DoesNotExist:
        cart = None

    return render(request, 'products/cart_detail.html', {
        'cart': cart
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    try:
        resident = Resident.objects.get(user=request.user)
    except Resident.DoesNotExist:
        messages.error(request, "You need to be associated with a resident account to add items to the cart.")
        return redirect('products:product_list')

    cart, created = Cart.objects.get_or_create(resident=resident)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if created:
        cart_item.quantity = 1  # Set the default quantity
    else:
        cart_item.quantity += 1  # Increment the quantity if the item already exists

    cart_item.save()  # Save the updated or newly created CartItem
    messages.success(request, "Item added to cart.")
    return redirect('products:cart_detail')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    try:
        resident = Resident.objects.get(user=request.user)
        cart = Cart.objects.get(resident=resident)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.delete()
        messages.success(request, "Item removed from cart.")
    except CartItem.DoesNotExist:
        messages.error(request, "Item not found in your cart.")

    return redirect('products:cart_detail')

@login_required
def checkout(request):
    try:
        resident = Resident.objects.get(user=request.user)
        cart = Cart.objects.get(resident=resident)
    except (Resident.DoesNotExist, Cart.DoesNotExist):
        messages.error(request, "You need a valid cart to proceed to checkout.")
        return redirect('products:cart_detail')

    if request.method == 'POST':
        for item in cart.items.all():
            total_price = item.total_price()
            Transaction.objects.create(
                buyer=resident,
                seller=item.product.added_by,
                product=item.product,
                quantity=item.quantity,
                total_price=total_price,
                payment_method='cash'  # Default payment method for this example
            )
        cart.items.all().delete()
        messages.success(request, "Checkout successful!")
        return redirect('products:transaction_list')

    return render(request, 'products/checkout.html', {
        'cart': cart
    })

