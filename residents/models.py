from django.contrib.auth.models import User
from django.db import models

class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    status_ownership = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Ensure the profile picture is named based on the Resident's ID
        if self.profile_picture:
            # Construct the file name using the resident's ID
            self.profile_picture.name = f'{self.id}.jpg'
        super().save(*args, **kwargs)