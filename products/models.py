from django.db import models

# Create your models here.
# products/models.py
from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_photo = models.ImageField(upload_to='products/', blank=True, null=True)
    product_type = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_weight = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
