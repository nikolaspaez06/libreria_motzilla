from django.shortcuts import render

from ..models.author import Author
from ..models.book import Book
from ..models.book_instance import BookInstance

def index(request):
    author = Author.objects.all()
    book = Book.objects.all()
    book_instance = BookInstance.objects.all()


    return render(
        request,
        'catalog/index.html',
        context=
        {
            'author':author,
            'book':book,
            'book_instance':book_instance
        }
    )


