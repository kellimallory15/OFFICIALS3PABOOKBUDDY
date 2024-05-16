from django.contrib import admin
from .models import Book, Author, Review, BookBuddy

class BookList(admin.ModelAdmin):
    list_display = ('author', 'series_num', 'genre', 'summary', 'publisher', 'published_date', 'page_total', 'title')
    list_filter = ('author', 'genre', 'series_num')
    search_fields = ('series_num', 'author', 'genre')
    ordering = ['series_num']

class AuthorList(admin.ModelAdmin):
    list_display = ('name', 'photo', 'birth_date', 'death_date', 'auth_id')
    list_filter = ('name', 'auth_id')
    search_fields = ('name', 'auth_id')
    ordering = ['auth_id']

class ReviewList(admin.ModelAdmin):
    list_display = ('book', 'user', 'title', 'text', 'rating', 'created_date', 'edited_date')
    list_filter = ('book', 'rating', 'title')
    search_fields = ('book', 'title')
    ordering = ['book']

class BookBuddyList(admin.ModelAdmin):
    list_display = ('book', 'user', 'fav_status', 'read_status', 'read_later_status', 'currently_reading', 'current_page', 'last_read')
    list_filter = ('book', 'user', 'read_status', 'fav_status')
    search_fields = ('book', 'fav_status', 'user')
    ordering = ['book']

admin.site.register(Book, BookList)
admin.site.register(Author, AuthorList)
admin.site.register(Review, ReviewList)
admin.site.register(BookBuddy, BookBuddyList)

