from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Tag, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom' )

@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'display_tags', 'price')

    def display_tags(self, obj):
        return ', '.join(tag.title for tag in obj.tags.all())

    display_tags.short_description = 'Tags'
