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

def filterbook(request, slug = None):
    if slug is None:
        search_queary = request.GET.get("search", "")
        data = {
        
            "generes":Genere.objects.all(),
            "books":Book.objects.filter(title__icontains = search_queary),
            "title": search_queary
        }
        return render(request, 'user_panel/filter.html', data)
    else:
        data = {
            
            "generes":Genere.objects.all(),
            "books":Book.objects.filter(genere__slug = slug),
            "title":Genere.objects.get(slug=slug).title
        }
        return render(request, 'user_panel/filter.html', data)