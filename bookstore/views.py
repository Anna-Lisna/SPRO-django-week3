from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from bookstore.forms import BookForm
from bookstore.models import Books, Authors


def show_books(request):
    books = Books.objects.all().order_by('-id')
    if request.method == "GET" and "search" in request.GET:
        search = request.GET['search']
        books = books.filter(title__contains=search)
    return render(request, 'bookstore/book_list.html', context={'books': books})


def book_detail(request, index):
    book = get_object_or_404(Books, id=index)
    author = book.author
    return render(request, 'bookstore/book_detail.html', context={'book': book, 'author': author})


def show_author(request, id):
    author = get_object_or_404(Authors, id=id)
    author_books = Books.objects.filter(author_id__exact=id)
    return render(request, 'bookstore/author.html', context={'author': author, 'author_books': author_books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    return render(request, 'bookstore/form.html', context={'book_form': BookForm})
