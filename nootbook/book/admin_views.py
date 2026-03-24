from django.shortcuts import render, redirect
from book.models import *
from .forms import *
from django.core.paginator import Paginator




def dashboard(request):
    return render(request, "admin/dashboard.html")

def manageGeneres(request):
    data = {}
    form = GenereForm(request.POST or None)
    generes = Genere.objects.all()
    paginator = Paginator(generes, 10)
    page_number = request.GET.get("page")
    genere_obj = paginator.get_page(page_number)
    data['generes'] = genere_obj
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            data = form.save(commit=False)
            data.slug = data.title.lower().replace(" ", "-")
            data.save()
            return redirect('manageGenere')
    return render(request, 'admin/manage_genere.html', data)

def manageAuthor(request):
    data = {}
    form = AuthorForm(request.POST or None)
    data['form'] = form
    authors = Author.objects.all()
    paginator = Paginator(authors, 8)
    page_number = request.GET.get("page")
    author_obj = paginator.get_page(page_number)

    data['authors'] = author_obj

    if request.method == 'POST':
        if form.is_valid():
            data = form.save(commit=False)
            data.slug = data.name.lower().replace(" ", "-")
            data.save()
            return redirect('manageAuthor')
    return render(request, 'admin/manage_author.html', data)

def manageBooks(request):
    data = {}
    books = Book.objects.all()
    # paginator 
    paginator = Paginator(books, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    data['books'] = page_obj
    return render(request, 'admin/manage_book.html', data)

def insertBook(request):
    data = {}
    form = BookForm(request.POST or None, request.FILES or None)
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            data = form.save(commit=False)
            data.slug = data.title.lower().replace(" ", "-")
            data.save()
            return redirect('manageBook')
    return render(request, 'admin/insertbook.html', data)