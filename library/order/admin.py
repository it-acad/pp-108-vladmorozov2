from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    # Define the list of fields to display in the admin list view
    list_display = ("id", "book", "user", "created_at", "end_at", "plated_end_at")

    # Add search functionality for user, book, and created_at fields
    search_fields = ("user__username", "book__name", "created_at")

    # Add filters for specific fields
    list_filter = ("created_at", "end_at")

    # Define the fieldsets to display them in separate sections
    fieldsets = (
        (
            "Order Information",
            {
                "fields": ("book", "user", "created_at"),
                "classes": ("wide", "extrapretty"),
            },
        ),
        (
            "Return Information123",
            {
                "fields": ("end_at", "plated_end_at"),
                "classes": ("wide",),
            },
        ),
    )

    # Customize the form layout (optional)


# Register the Order model with the admin site
admin.site.register(Order, OrderAdmin)
