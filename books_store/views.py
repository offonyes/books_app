from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from books_store.models import Books, Author, Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic.list import ListView


# Create your views here.
class BaseListView(ListView):
    paginate_by = 3

    def get_paginate_orphans(self):
        return 0

    def get_allow_empty(self):
        return True

    def paginate_queryset(self, queryset, page_size):
        paginator = self.get_paginator(
            queryset,
            page_size,
            orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty(),
        )
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
        try:
            page_number = int(page)
        except ValueError:
            if page == "last":
                page_number = paginator.num_pages
            else:
                page_number = 1
        try:
            page = paginator.page(page_number)
            return paginator, page, page.object_list, page.has_other_pages()
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
            return paginator, page, page.object_list, page.has_other_pages()


class BookListView(BaseListView):
    model = Books
    context_object_name = 'page'
    template_name = 'store/books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of Books'
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.get_selected_category()
        context['selected_author'] = self.get_selected_author()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        author_id = self.request.GET.get('author')

        if category_id:
            queryset = queryset.filter(category__id=category_id)
        if author_id:
            queryset = queryset.filter(author__id=author_id)

        return queryset.distinct()

    def get_selected_category(self):
        try:
            return int(self.request.GET.get('category'))
        except TypeError:
            return None

    def get_selected_author(self):
        try:
            return int(self.request.GET.get('author'))
        except TypeError:
            return None


class AuthorListView(BaseListView):
    model = Author
    context_object_name = 'page'
    template_name = 'store/authors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of Authors'
        return context


def index(request):
    return render(request, 'store/index.html')


def about_page(request):
    return render(request, 'store/about.html')


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
    return render(request, 'store/search.html', {'books': books, 'query': query})
