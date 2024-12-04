from django import forms
from django.contrib.auth.models import User
from .models import Resident

class ResidentRegistrationForm(forms.ModelForm):
    # Password confirmation fields
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User  # We'll create the User model first
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        # Save the User object first
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        
        # Create the Resident object
        resident = Resident(
            user=user,
            phone_number=self.cleaned_data['phone_number'],
            address=self.cleaned_data['address'],
            status_ownership=self.cleaned_data['status_ownership']
        )
        if commit:
            resident.save()
        return user

from django import forms

class ResidentLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
