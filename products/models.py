from django.db import models
from residents.models import Resident 

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_photo = models.ImageField(upload_to='products/', blank=True, null=True)
    product_type = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_weight = models.DecimalField(max_digits=6, decimal_places=2)
    added_by = models.ForeignKey(Resident, on_delete=models.CASCADE)  
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

class Transaction(models.Model):
    buyer = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='buyer_transactions')
    seller = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='seller_transactions')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='transactions')
    transaction_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('gopay', 'Gopay'),
        ('ovo', 'OVO'),
        ('cash', 'Cash'),
    ])

    def __str__(self):
        return f"{self.buyer} bought {self.product} from {self.seller} on {self.transaction_date}"

class Cart(models.Model):
    resident = models.OneToOneField(Resident, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"Cart of {self.resident}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.product_price

    def __str__(self):
        return f"{self.quantity} of {self.product.product_name}"