from django.shortcuts import render, redirect
from book.models import *
from .forms import *
from django.core.paginator import Paginator
from django.contrib.auth.models import User

from django.http import HttpResponseForbidden
from functools import wraps

def superuser_require(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You must be logged in to access this page.")
        if not request.user.is_superuser:
            return HttpResponseForbidden("You do not have permission to access this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view


@superuser_require
def dashboard(request):
    data = {
        "books":Book.objects.count(),
        "generes":Genere.objects.count(),
        "users":User.objects.count(),
        "authors":Author.objects.count(),

    }
    return render(request, "admin/dashboard.html", data)

@superuser_require
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

@superuser_require
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


@superuser_require
def manageBooks(request):
    data = {}
    books = Book.objects.all()
    # paginator 
    paginator = Paginator(books, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    data['books'] = page_obj
    return render(request, 'admin/manage_book.html', data)

@superuser_require
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

@superuser_require
def updateBook(request, id):
    books = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=books)
    if form.is_valid():
        data = form.save(commit=False)
        data.slug = data.title.lower().replace(" ", "-")
        data.save()
        return redirect('manageBook')
    return render(request, "admin/update_book.html", {'form':form})

@superuser_require
def updateGenere(request, id):
    generes = Genere.objects.get(id=id)
    form = GenereForm(request.POST or None, instance=generes)
    
    if form.is_valid():
        data = form.save(commit=False)
        data.slug = data.title.lower().replace(" ", "-")
        data.save()
        return redirect('manageGenere')

    return render(request, "admin/update_genere.html", {'form':form})

@superuser_require
def updateAuthor(request, id):
    authors = Author.objects.get(id=id)
    form = AuthorForm(request.POST or None, instance=authors, )
    
    if form.is_valid():
        data = form.save(commit=False)
        data.slug = data.name.lower().replace(" ", "-")
        data.save()
        return redirect('manageAuthor')

    return render(request, "admin/update_author.html", {'form':form})

@superuser_require
def deleteBook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('manageBook')