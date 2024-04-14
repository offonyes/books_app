from django.contrib import admin
from django.utils.html import mark_safe
from books_store.models import Books, Author, Category


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'get_categories', 'price', 'cover_type', 'image_preview']
    search_fields = ['name', 'author__name']
    list_filter = ['category', 'author']
    list_editable = ['price', 'cover_type']

    # In adding and change pages
    # fields = ['name', 'author_name','price', 'image']
    # readonly_fields = ['name', 'price']

    # Метод для получения строкового представления категорий книги
    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])

    get_categories.short_description = 'Category'

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


class CategotyrAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Books, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategotyrAdmin)
