from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from announcements.models import Announcement  # Import announcements model

def home(request):
    # Fetch announcements (customize as needed)
    announcements = Announcement.objects.order_by('-date')[:3]
    return render(request, 'home.html', {'announcements': announcements})
