from django.contrib import admin
from .models import *
class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
    search_fields = ('title',)

class BookInline(admin.StackedInline):
    model = Book
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['last_name', 'first_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','book', 'status','borrowed', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            "fields": (
                'id','book','imprint'
            ),
        }),
        ('Availability', {
            "fields": (
                'due_back','status','borrowed'
            ),
        }),

    )
    
    
admin.site.register(Genre)
admin.site.register(Language)
