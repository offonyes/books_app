from django.http import JsonResponse
from django.shortcuts import render
from market.models import Books


# Create your views here.


def book_list(request):
    books = Books.objects.all()
    context = [{'id': book.id, 'name': book.name, 'page_count': book.page_count, 'category': book.category,
                'author_name': book.author_name, 'price': str(book.price), 'image': book.image.url}
               for book in books]
    return JsonResponse(context, safe=False)


def book_detail(request, book_id):
    book = Books.objects.get(id=book_id)
    context = {'id': book.id, 'name': book.name, 'page_count': book.page_count, 'category': book.category,
               'author_name': book.author_name, 'price': str(book.price), 'image': book.image.url}
    return JsonResponse(context)


def author_list(request):
    authors = Books.objects.values_list('author_name', flat=True).distinct()
    context = {'authors': authors}
    return render(request, 'author_list.html', context)


def author_books(request, author_name):
    books = Books.objects.filter(author_name=author_name)
    context = {'author_name': author_name, 'books': books}
    return render(request, 'author_books.html', context)
