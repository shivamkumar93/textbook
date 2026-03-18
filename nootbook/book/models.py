from django.db import models

# Create your models here.

class Genere(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    slug = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    price = models.FloatField()
    dis_price = models.FloatField(null=True, blank=True)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")
    genere = models.ForeignKey(Genere, on_delete=models.CASCADE, related_name="category")
    cover_image = models.ImageField(upload_to="book/cover")
    edition = models.CharField(default="larest update")
    isbn = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}-- {self.author}"