from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "last_name", "role", "is_active")
    list_filter = ("role", "is_active")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("id",)

    def save_model(self, request, obj, form, change):
        if obj.password:  # If password is provided, make sure it's hashed
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = "Full Name"
