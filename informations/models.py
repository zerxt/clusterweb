from django.db import models

# Create your models here.
from django.db import models

class Information(models.Model):
    subject = models.CharField(max_length=255)
    aspiration_message = models.TextField()
    photo = models.ImageField(upload_to='information_center_photos/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject