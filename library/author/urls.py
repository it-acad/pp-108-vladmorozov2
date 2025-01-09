from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_authors, name="list_authors"),
    path("create/", views.create_author, name="create_author"),
    path(
        "<int:author_id>/delete/",
        views.delete_author,
        name="delete_author",
    ),
]
