from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from books_store.models import Books, Author
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def book_list1(request):
    book = Books.objects.all()
    serialized_book = serialize('json', book)
    return JsonResponse(serialized_book, safe=False)

def book_detail(request, book_id):
    try:
        book = Books.objects.get(id=book_id)
        context = {'id': book.id, 'book_name': book.book_name, 'page_count': book.page_count, 'category': book.category,
               'author': book.author.name, 'price': str(book.price), 'image': book.image.url}
    except Books.DoesNotExist:
        context= {'error_message': 'object not found'}
    return JsonResponse(context)

from django.views.generic.list import ListView
from django.core.paginator import Paginator
from .models import Books

class BookListView(ListView):
    model = Books
    context_object_name = 'page'  
    template_name = 'store/books.html'
    paginate_by = 3
    extra_contetxt = {'custom_title': 'List of Books', 'cat_selected': 2}

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        return context

def author_detail(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
        print(author)
        context = {'id': author.id, 'author_name': author.name, 'description': author.description, 'wiki_page': author.wiki_page,
               'number_of_books': str(author.number_of_books), 'image': author.image.url}
    except Books.DoesNotExist:
        context= {'error_message': 'object not found'}
    return JsonResponse(context)

def author_list(request):
    queryset = Author.objects.all()
    paginator = Paginator(queryset, 3)  
    page_number = request.GET.get('page')  
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    print(page.object_list)
    return render(request, 'store/authors.html', {'page': page})


def author_books(request, author):
    books = Books.objects.filter(author=author)
    context = {'author': author, 'books': books}
    return render(request, 'author_books.html', context)
