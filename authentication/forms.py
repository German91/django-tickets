from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password2 != password1:
            raise forms.ValidationError('Password does not match')
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username)

        if user:
            raise forms.ValidationError('Username already in use')
        return username

class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(label='New Password', min_length=6, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', min_length=6, widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password2 != password1:
            raise forms.ValidationError('Password does not match')
        return password2