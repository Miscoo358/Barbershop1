from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    """Handles user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log the user in after registration
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    """Handles user login."""
    if request.method == 'POST':
        # Pass the request to AuthenticationForm to get proper error messages
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def home_view(request):
    """
    Displays a success page for regular users and an admin dashboard for staff/superuser.
    Regular users see an "Authentication Success" message and are redirected to index.html.
    Admin users see options for admin control, process receipt, and print report.
    """
    if request.user.is_staff or request.user.is_superuser:
        return render(request, 'accounts/admin_dashboard.html')
    else:
        return render(request, 'accounts/auth_success.html')
