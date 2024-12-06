from django.contrib import admin
from .models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('announcementTitle', 'writer', 'date', 'photo')
    search_fields = ('announcementTitle', 'writer')
    list_filter = ('date',)
    ordering = ('-date',)
    fields = ('announcementTitle', 'message', 'photo', 'writer')  # Custom form layout

# Register the Announcement model with the admin
admin.site.register(Announcement, AnnouncementAdmin)
