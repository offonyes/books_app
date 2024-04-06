from django.urls import path
from market.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('authors/', author_list, name='author_list'),
    path('authors/<str:author_name>/', author_books, name='author_books'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
