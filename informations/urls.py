from django.urls import path
from . import views

app_name = 'informations'

urlpatterns = [
    path('', views.information_list, name='information_list'),  # List posts
    path('create/', views.create_information, name='create_information'),  # Create a post
]
