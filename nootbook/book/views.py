from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    data = {
        "title":"home",
        "generes":Genere.objects.all(),
        "books":Book.objects.all()
    }
    return render(request, 'user_panel/home.html', data)