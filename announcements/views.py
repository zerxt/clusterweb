from django.shortcuts import render, redirect
from .forms import AnnouncementForm
from .models import Announcement

def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-date')  # Ensure this returns results
    return render(request, 'announcements/announcement_list.html', {'announcements': announcements})


def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('announcements:announcement_list')  # Redirect to the list of announcements after saving
    else:
        form = AnnouncementForm()

    return render(request, 'announcements/create_announcement.html', {'form': form})
