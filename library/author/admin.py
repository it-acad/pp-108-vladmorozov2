from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Author model.
    """

    # Fields to display in the list view
    list_display = ("id", "name", "surname", "patronymic", "get_books")

    # Fields to enable searching
    search_fields = ("name", "surname", "patronymic")

    # Fields to filter by in the admin list view
    list_filter = ("books",)

    # Read-only fields (if needed, like 'id')
    readonly_fields = ("id",)

    # Fieldsets for better organization
    fieldsets = (
        ("Personal Information", {"fields": ("name", "surname", "patronymic")}),
        ("Books", {"fields": ("books",)}),
    )

    def get_books(self, obj):
        """
        Custom method to display books related to the author.
        """
        return ", ".join([book.name for book in obj.books.all()])

    get_books.short_description = "Books"
