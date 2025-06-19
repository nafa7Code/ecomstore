from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'phone_number', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('معلومات إضافية', {'fields': ('phone_number', 'address', 'is_verified')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
