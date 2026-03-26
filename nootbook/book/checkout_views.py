from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def addTocart(request, slug):
    book = get_object_or_404(Book, slug=slug)

    if book:
        order_queary = Order.objects.filter(user=request.user, payment_id = None)
        if order_queary.exists():
            order = order_queary[0]
            order_itme_queary = OrderItem.objects.filter(order_id=order, book_id=book)
            if order_itme_queary.exists():
                order_item = order_itme_queary[0]
                order_item.quantity +=1
                order_item.save()
            else:
                OrderItem.objects.create(order_id=order, book_id=book, quantity=1)
        else:
            order = Order.objects.create(user=request.user, total_price = 0)
            OrderItem.objects.create(order_id=order, book_id=book, quantity=1)

    else:
        return redirect("bookview", slug=slug)
    return redirect('cart')




@login_required
def minusTocart(request):
    pass

@login_required
def removeFromcart(request):
    pass

@login_required
def checkout(request):
    pass

@login_required
def applyCoupon(request):
    pass

@login_required
def removeCoupon(request):
    pass