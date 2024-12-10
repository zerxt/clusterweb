from django.urls import path
from . import views

app_name = 'informations'

urlpatterns = [
    path('create/', views.create_information, name='create_information'),  # Create a post
]
