from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    # Define fieldsets to separate static and dynamic information
    fieldsets = (
        (
            "Static Information",
            {
                "fields": (
                    "name",
                    "description",
                ),
                "classes": (
                    "wide",
                    "extrapretty",
                ),  # Optional: Adds some visual styling
            },
        ),
        (
            "Dynamic Information",
            {
                "fields": ("count",),
                "classes": ("wide",),
            },
        ),
    )

    # Customize the list display in the Admin list view
    list_display = (
        "id",
        "name",
        "description",
        "count",
    )

    # Enable search by book title and description
    search_fields = ["name", "description"]

    # Add a filter option for the list view
    list_filter = ["count"]

    class Media:
        # Link the custom CSS file for the Admin panel
        css = {"all": (r"library\book\admin.css",)}  # Adjust the path as necessary


# Register the Book model with the admin
admin.site.register(Book, BookAdmin)
