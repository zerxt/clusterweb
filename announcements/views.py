from django.shortcuts import render, redirect
from .forms import AnnouncementForm
from .models import Announcement

def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-date')  # Ensure this returns results
    return render(request, 'announcements/announcement_list.html', {'announcements': announcements})