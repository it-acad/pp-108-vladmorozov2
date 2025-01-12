from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_all_books, name="show_all_books"),
    path("<int:book_id>/", views.book_details, name="book_detail"),
]
