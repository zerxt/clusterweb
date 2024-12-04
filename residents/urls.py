from django.urls import path
from . import views

app_name = 'residents'  # This ensures namespacing is used correctly

urlpatterns = [
    path('login/', views.login_resident, name='login_resident'),  # Ensure this is defined
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_resident, name='logout_resident'),
]
