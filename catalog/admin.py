from django.contrib import admin


from .models.book import Book
from .models.author import Author
from .models.book_instance import BookInstance
from .models.language import Language
from .models.genre import Genre


admin.site.register (Book)
admin.site.register (Author)
admin.site.register (BookInstance)
admin.site.register (Language)
admin.site.register (Genre)
