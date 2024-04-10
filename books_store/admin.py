from django.contrib import admin
from django.utils.html import mark_safe
from books_store.models import Books, Author


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'author', 'category', 'price', 'image_preview']
    search_fields = ['book_name', 'author']
    list_filter = ['category', 'price']
    list_editable = ['price']

    # In adding and change pages
    # fields = ['name', 'author_name','price', 'image']
    # readonly_fields = ['name', 'price']
    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{url}" width="80" height="120" />'.format(url=obj.image.url))
        else:
            return 'No Image'

    image_preview.short_description = 'Image'

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'number_of_books', 'image_preview']
    search_fields = ['name']
    list_editable = ['description']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{url}" width="100" height="120" />'.format(url=obj.image.url))
        else:
            return 'No Image'

    image_preview.short_description = 'Image'

admin.site.register(Books, BookAdmin)
admin.site.register(Author, AuthorAdmin)
