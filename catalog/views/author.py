from django.views import generic

from ..models.author import Author

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'catalog/author/author_list.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    context_object_name = 'author_detail'
    template_name = 'catalog/author/author_datail.html'


class AuthorCreateView(generic.CreateView):
    model = Author
    fields=[
        'name',
        'date_of_birth',
        'data_of_death'
        ]
    template_name = 'catalog/author/author_form.html'

            
        
        