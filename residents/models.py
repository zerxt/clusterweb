from django.contrib.auth.models import User
from django.db import models

class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    status_ownership = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
