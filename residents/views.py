from django.shortcuts import render, redirect
from .forms import ResidentRegistrationForm
from .forms import ResidentLoginForm
from .forms import AccountEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request, 'residents/dashboard.html')

def register(request):
    if request.method == 'POST':
        form = ResidentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # This will save the User and Resident
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('residents:login')  # Redirect to login page after registration
    else:
        form = ResidentRegistrationForm()

    return render(request, 'residents/register.html', {'form': form})


def login_resident(request):
    if request.method == 'POST':
        form = ResidentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('residents:dashboard')  # Redirect to the information list after login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = ResidentLoginForm()

    return render(request, 'residents/login.html', {'form': form})

def logout_resident(request):
    logout(request)
    return redirect('residents:login') 


@login_required
def edit_account(request):
    user = request.user
    resident = user.resident

    if request.method == 'POST':
        user_form = AccountEditForm(request.POST, request.FILES, instance=resident)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Your account details have been updated.")
            return redirect('residents:edit')
    else:
        user_form = AccountEditForm(instance=resident)

    return render(request, 'residents/edit_account.html', {
        'user_form': user_form,
    })