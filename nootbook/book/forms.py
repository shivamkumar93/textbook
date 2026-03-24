from django.forms import ModelForm
from .models import *

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