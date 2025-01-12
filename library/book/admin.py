from django.contrib import admin
from .models import Book


# Customizing the Book admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "count",
    )  # Fields to display in the list view
    search_fields = ("name", "description")  # Search functionality
    list_filter = ("count",)  # Optional: add filtering by count or other fields
    ordering = ("id",)  # Ordering the records

    # Optional: To allow authors to be managed through the Book model
    # If you have an authors field as a Many-to-Many relation
    filter_horizontal = ("authors",)


# Register the Book model with the custom BookAdmin configuration
admin.site.register(Book, BookAdmin)
