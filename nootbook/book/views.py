from django.shortcuts import render
from .models import *
import re

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
        if search_queary:
            if re.match(r"^[0-9]{10}(\d{3})?$",search_queary):
                try:
                    data = {}
                    book = Book.objects.get(isbn=search_queary)
                    data['book'] = book
                    data['generes'] = Genere.objects.all()
                    data['related_books'] = Book.objects.filter(genere=book.genere).exclude(slug=book.slug)[:6]
                    return render(request, "user_panel/bookview.html", data)

                except Book.DoesNotExist:
                    pass
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
    
def bookview(request, slug):
    data = {
     
        "generes":Genere.objects.all(),
        "book":Book.objects.get(slug=slug),
        "related_books":Book.objects.filter(genere=Book.objects.get(slug=slug).genere).exclude(slug=slug)[:4]
    }
    return render(request, 'user_panel/bookview.html', data)