from django.db import models
from .book import Book
from django.urls import reverse

class BookInstance(models.Model):
    unique_id = models.CharField(max_length=50)
    due_back = models.DateField(default=0)
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
    book = models.ForeignKey(Book, null = True, on_delete=models.SET_NULL)
    imprint = models.CharField(max_length=50)
    borrower = models.CharField(max_length=30)

    def __str__(self):
        return self.unique_id
    
    def get_absolute_url(self):
        return reverse("book_instance_detail", args=[str(self.id)])