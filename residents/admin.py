from django.contrib import admin
from .models import Resident

@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address', 'status_ownership')
    search_fields = ('user__username', 'phone_number', 'status_ownership')
    list_filter = ('status_ownership',)
