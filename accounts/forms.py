from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Confirm Password'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Password'}))