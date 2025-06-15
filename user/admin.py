from django.contrib import admin

# Register your models here.

from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)
    list_filter = ('created_at',)

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'address', 'profession', 'created_at')
    search_fields = ('name', 'email', 'mobile', 'profession')
    ordering = ('-created_at',)
    list_filter = ('created_at',)
