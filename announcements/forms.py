# forms.py
from django import forms
from .models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['announcementTitle', 'message', 'photo', 'writer']
