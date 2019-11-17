from django.contrib import admin

from catalog.models import Author, Genre, Book, BookInstance, Language
from django.contrib.admin.options import ModelAdmin

class BooksInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death', 'author_image', 'biography')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death'), 'image', 'biography']
    inlines = [BooksInline]


# Register the admin class with the associated model



class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language', 'book_cover', 'summary')
    inlines = [BooksInstanceInline]
    
    



    

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )





admin.site.register(Genre)

admin.site.register(Language)