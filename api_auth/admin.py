from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Configure user admin display


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = (
        "email",
        "user_name",
    )
    list_filter = ("email", "user_name", "is_active", "is_staff")
    ordering = ("-start_date",)
    list_display = ("email", "id", "user_name", "is_active", "is_staff")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "user_name",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "user_name",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


# Register user model.
admin.site.register(User, UserAdminConfig)
