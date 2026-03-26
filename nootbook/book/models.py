from django.db import models
from django.contrib.auth.models import User

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
    
class Address(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    addess_line1 = models.CharField(max_length=200)
    addess_line2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Coupon(models.Model):
    code = models.CharField(max_length=100, unique=True)
    discount_amount = models.FloatField()
    valid_from = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)
    mode = models.CharField(max_length=50)
    trancation_id = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment {self.id} - {self.amount}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField()
    order_date = models.DateTimeField(auto_now_add=True)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)
    coupon_id = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True, blank=True)
    address_is = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Order {self.user.username}- {self.total_price}"
    
class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="books")
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"OrderItme {self.order_id.id} - {self.book_id.title} - Quantity: {self.quantity}"