from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import RegisterForm


def register(request):
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