from django.urls import path
from . import views

app_name = 'residents'  # Add this to namespace the URLs

urlpatterns = [
    path('login/', views.login_resident, name='login'),  # Use 'login' as the name for consistency
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_resident, name='logout'),  # Change to 'logout' for consistency
]
