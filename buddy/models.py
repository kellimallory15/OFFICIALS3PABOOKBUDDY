from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    birth_date = models.DateField(default=timezone.now)
    death_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=50)
    auth_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.name}' ## Potentially specify different return

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_authors')
    series_num = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1)])
    genre = models.CharField(max_length=50)
    summary = models.CharField(max_length=500)
    publisher = models.CharField(max_length=50)
    published_date = models.DateField(default=timezone.now)
    page_total = models.IntegerField(blank=False, default=0, null=False)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_review')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    rating = models.IntegerField(blank=False, null=False, default=1,
                                 validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Review for "{self.book.title} by {self.user.username}'

    def reader_reviews(self):
        return str(self.user.username)

class BookBuddy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='buddy_book')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_status = models.BooleanField(default=False, null=True)
    read_status = models.BooleanField(default=False, null=True)
    read_later_status = models.BooleanField(default=False, null=True)
    currently_reading = models.BooleanField(default=False, null=True)
    current_page = models.IntegerField(default=0, null=True, blank=False)
    last_read = models.DateField(auto_now=False)

    def __str__(self):
        return f'{self.user.username} - "{self.book.title}" (Fav: {self.fav_status}, Reading: {self.currently_reading})'

    ## Define null statuses for above booleans // identify date modifications required for last read
