from django.contrib import admin

from .models import Author, Publisher, Book, Store, Stock

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Store)
admin.site.register(Stock)

