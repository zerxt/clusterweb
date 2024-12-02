from django import forms
from .models import Information

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['subject', 'aspiration_message', 'photo']
