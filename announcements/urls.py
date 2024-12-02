from django.urls import path
from . import views

app_name = 'announcements'

urlpatterns = [
    path('create/', views.create_announcement, name='create_announcement'),
]