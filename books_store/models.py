from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Author Name')
    image = models.ImageField(upload_to='authors/', null=True, blank=True, verbose_name='Image')
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    wiki_page = models.URLField(max_length=200, null=True, blank=True, verbose_name='Wiki Page')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']

    @property
    def number_of_books(self):
        return self.books.count()


class Books(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Book Name')
    page_count = models.IntegerField(null=True, verbose_name='Page Count')
    category = models.CharField(max_length=100, null=False, blank=False, verbose_name='Category')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, verbose_name='Price')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['name', 'price', 'page_count']
        indexes = [
            models.Index(fields=['name'], name='name_idx'),
            models.Index(fields=['price'], name='price_idx'),
        ]
        constraints = [
            models.UniqueConstraint(fields=['name', 'author'], name='unique_book')
        ]
