from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)  # Added isbn field
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

class Store(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, through='Stock')

class Stock(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    stock = models.IntegerField()

