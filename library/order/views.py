# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Book, CustomUser
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test


def is_librarian(user):
    return user.is_authenticated and user.role == 1  # Check if role is 'Librarian'


@user_passes_test(is_librarian)
def show_all_orders(request):
    orders = Order.objects.all()  # Get all orders from the database
    context = {"orders": orders}
    return render(request, "order/show_all_orders.html", context)


def show_my_orders(request):
    user = request.user  # Get the logged-in user
    orders = Order.objects.filter(user=user)  # Get orders related to the user
    context = {"orders": orders}
    return render(request, "order/show_my_orders.html", context)


def create_order(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        plated_end_at = request.POST.get("plated_end_at")
        book = Book.objects.get(id=book_id)
        user = request.user  # The logged-in user

        # Check if the book is available
        if book.count > 0:
            order = Order.objects.create(
                user=user, book=book, plated_end_at=plated_end_at
            )
            return redirect("show_my_orders")  # Redirect to the user's orders page
        else:
            # Handle case where book is not available
            return render(
                request, "order/create_order.html", {"error": "Book is not available."}
            )

    books = Book.objects.all()  # Get all books for the user to choose from
    return render(request, "order/create_order.html", {"books": books})


def close_order(request, order_id):
    # Fetch the order by its ID
    order = get_object_or_404(Order, id=order_id)

    # Check if the order is not closed (end_at is None)
    if not order.end_at:
        # Set the end_at field to the current time
        order.end_at = timezone.now()
        order.save()

    # After closing, redirect to the orders list
    return redirect("show_all_orders")
