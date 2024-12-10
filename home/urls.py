# In an existing app's urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage URL
]
