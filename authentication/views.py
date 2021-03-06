"""
Register, update user profile
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegisterForm, ChangePasswordForm


def register(request):
    """
    Create new user
    """
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = form.save(commit=False)
            user.set_password(password)
            user.save()

            auth = authenticate(username=username, password=password)

            if auth is not None:
                login(request, auth)
                return redirect('ticket_list')
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    """
    Edit user profile
    """
    if request.method == 'POST':
        user = get_object_or_404(User, username=request.user.username)
        user.username = request.POST.get('username')
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Username successfully updated')
    return render(request, 'auth/profile.html')

@login_required
def change_password(request):
    form = ChangePasswordForm()
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            user = get_object_or_404(User, username=request.user.username)
            user.set_password(password1)
            user.save()

            auth = authenticate(username=user.username, password=password1)

            if auth is not None:
                login(request, auth)
                messages.add_message(request, messages.SUCCESS, 'Password successfully changed')
    return render(request, 'auth/change_password.html', {'form': form})
            