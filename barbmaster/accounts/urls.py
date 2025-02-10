from django.urls import path
from .views import home_view, login_view, register_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    # Add any other URL patterns if needed
]
