from django.urls import path
from . import views

app_name = 'announcements'

urlpatterns = [
    path('', views.announcement_list, name='announcement_list'),  # List announcements
    path('create/', views.create_announcement, name='create_announcement'),  # Create an announcement
]
