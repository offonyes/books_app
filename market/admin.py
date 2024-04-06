from django.contrib import admin
from django.utils.html import mark_safe
from market.models import Books


# Register your models here.

# @admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author_name', 'category', 'price']
    search_fields = ['name', 'author_name']
    list_filter = ['category', 'price']
    list_editable = ['price']

    # In adding and change pages
    # fields = ['name', 'author_name','price', 'image']
    # readonly_fields = ['name', 'price']
    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{url}" width="100" height="100" />'.format(url=obj.image.url))
        else:
            return 'No Image'

    image_preview.short_description = 'Image'


admin.site.register(Books, BookAdmin)
