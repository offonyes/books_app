from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from books_store.models import Books, Author
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic.list import ListView


# Create your views here.
class BookListView(ListView):
    model = Books
    context_object_name = 'page'
    template_name = 'store/books.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['title'] = 'List of Books'
        return context


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


def index(request):
    return render(request, 'store/index.html')


def about_page(request):
    return render(request, 'store/about.html')


def book_list1(request):
    book = Books.objects.all()
    serialized_book = serialize('json', book)
    return JsonResponse(serialized_book, safe=False)


def book_detail(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    return render(request, 'store/book.html', {'book': book})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'store/Author.html', {'author': author})


def search_results(request):
    query = request.GET.get('search')
    book_list = Books.objects.filter(name__icontains=query)

    paginator = Paginator(book_list, 4)
    page = request.GET.get('page')

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    print(books.object_list)
    return render(request, 'store/search.html', {'books': books, 'query': query})
