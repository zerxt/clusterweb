from django.contrib import admin
from .models import Information  # Correctly import the Information model

class InformationAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date_posted', 'added_by', 'aspiration_message')
    search_fields = ('subject', 'added_by__name')  # Assuming Resident has a 'name' field
    list_filter = ('date_posted',)

admin.site.register(Information, InformationAdmin)
