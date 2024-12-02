from .models import Information
from .forms import InformationForm
from django.shortcuts import render, redirect

def information_list(request):
    posts = Information.objects.all().order_by('-date_posted')
    return render(request, 'informations/information_list.html', {'posts': posts})

def create_information(request):
    if request.method == 'POST':
        form = InformationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Correct redirect to the information list page
            return redirect('informations:information_list')

    else:
        form = InformationForm()
    return render(request, 'informations/create_information.html', {'form': form})