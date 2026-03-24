from django.shortcuts import render, redirect
from book.models import *

def dashboard(request):
    return render(request, "admin/dashboard.html")

def manageGeneres(request):
    data = {}
    data['generes'] = Genere.objects.all()
    return render(request, 'admin/manage_genere.html', data)

def manageAuthor(request):
    data = {}
    data['authors'] = Author.objects.all()
    return render(request, 'admin/manage_author.html', data)

def manageBooks(request):
    data = {}
    data['books'] = Book.objects.all()
    return render(request, 'admin/manage_book.html', data)