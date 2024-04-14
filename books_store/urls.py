from django.urls import path
from books_store.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('about/', about_page, name='about'),
    path('search/', search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
