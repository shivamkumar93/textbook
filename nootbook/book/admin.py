from django.contrib import admin
from .models import *
# Register your models here.

class GenereAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Genere, GenereAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "slug")
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title","slug","price","dis_price","author","genere","isbn")
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Book, BookAdmin)

admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Coupon)
admin.site.register(Payment)