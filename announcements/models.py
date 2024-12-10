from django.db import models

class Announcement(models.Model):
    announcementTitle = models.CharField(max_length=255)
    message = models.TextField()
    photo = models.ImageField(upload_to='announcements/', null=True, blank=True)  # Optional image
    writer = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)  # Automatically sets the date when the announcement is created

    def __str__(self):
        return self.announcementTitle
