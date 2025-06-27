from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

# Unregister the default User admin
admin.site.unregister(User)

# Register your custom User admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):  # optionally inherit from UserAdmin to keep default features
    list_display = ('username', 'email', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_active',)
