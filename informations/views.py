from django.contrib.auth.decorators import login_required
from .models import Information
from .forms import InformationForm
from django.shortcuts import render, redirect
from residents.models import Resident
from django.contrib import messages

def information_list(request):
    posts = Information.objects.all().order_by('-date_posted')
    return render(request, 'informations/information_list.html', {'posts': posts})

@login_required
def create_information(request):
    if request.method == 'POST':
        form = InformationForm(request.POST, request.FILES)
        if form.is_valid():
            information = form.save(commit=False)  # Don't save yet
            try:
                # Attach the current resident to the added_by field
                information.added_by = Resident.objects.get(user=request.user)
                information.save()
                messages.success(request, "Information created successfully!")
                return redirect('informations:information_list')
            except Resident.DoesNotExist:
                messages.error(request, "Current user is not associated with any resident account.")
                return redirect('informations:create_information')
    else:
        form = InformationForm()
    return render(request, 'informations/create_information.html', {'form': form})
