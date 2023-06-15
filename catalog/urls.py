from django.urls import path

from .views import views
from .views import author
from .views import book_instance
from .views import book

urlpatterns = [
    path ('',views.index,name= "index")
]


urlpatterns += [
    path("author",author.AuthorListView.as_view(),name="author"),
    path("author/<int:pk>",author.AuthorDetailView.as_view(),name='author-detail'),
    path("author/create",author.AuthorCreateView.as_view(),name = 'create-person')
]


urlpatterns += [
    path("book",book.BookListView.as_view(),name='book'),
    path("book/<int:pk>",book.BookDetailtView.as_view(),name='book_detail'),
    path("book/create",book.BookCreateView.as_view(),name= 'create_book')
]