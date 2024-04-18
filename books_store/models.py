from django.db import models
from django.utils.translation import gettext_lazy as _
from books_store.choice import *


class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Author Name'))
    image = models.ImageField(upload_to='authors/', null=True, blank=True, verbose_name=_('Image'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    wiki_page = models.URLField(max_length=200, null=True, blank=True, verbose_name=_('Wiki Page'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')
        ordering = ['name']

    @property
    def number_of_books(self):
        return self.books.count()


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Category Name'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Books(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Book Name'))
    page_count = models.IntegerField(null=True, verbose_name=_('Page Count'))
    # Many-to-Many
    category = models.ManyToManyField(Category, related_name='books', verbose_name=_('Category'))
    # Foreign Key
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name=_('Author'))
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, verbose_name=_('Price'))
    cover_type = models.CharField(max_length=10, choices=COVER_TYPES, default='soft', verbose_name=_('Cover Type'))
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name=_('Image'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
        ordering = ['name', 'price', 'page_count']
        indexes = [
            models.Index(fields=['name'], name='name_idx'),
            models.Index(fields=['price'], name='price_idx'),
        ]
        constraints = [
            models.UniqueConstraint(fields=['name', 'author'], name='unique_book')
        ]
