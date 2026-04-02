from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active')

    # 🔥 Add role to editable fields
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )

    # 🔥 Optional: allow quick edit from list view
    list_editable = ('role', 'is_active')


admin.site.register(User, CustomUserAdmin)