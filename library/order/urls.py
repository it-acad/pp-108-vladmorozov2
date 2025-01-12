from django.urls import path
from . import views

urlpatterns = [
    path(
        "orders/", views.show_all_orders, name="show_all_orders"
    ),  # Librarian view to show all orders
    path(
        "my-orders/", views.show_my_orders, name="show_my_orders"
    ),  # User view to show their orders
    path(
        "create-order/", views.create_order, name="create_order"
    ),  # User view to create an order
    path(
        "close-order/<int:order_id>/", views.close_order, name="close_order"
    ),  # Librarian view to close order
]
