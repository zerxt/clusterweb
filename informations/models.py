from django.db import models
from residents.models import Resident 


class Information(models.Model):
    subject = models.CharField(max_length=255)
    aspiration_message = models.TextField()
    photo = models.ImageField(upload_to='information_center_photos/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(Resident, on_delete=models.CASCADE)  

    def __str__(self):
        return self.subject