from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django import forms

class GenereForm(ModelForm):
    class Meta:
        model = Genere
        exclude = ['slug']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        exclude = ['slug']

class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ['slug']

class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']