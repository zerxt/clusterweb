from django.shortcuts import render
# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .forms import AnnouncementForm

def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('announcements:announcement_list')  # Redirect to the list of announcements after saving
    else:
        form = AnnouncementForm()

    return render(request, 'announcements/create_announcement.html', {'form': form})
