from django.contrib import admin

# Register your models here.
from .models import Tenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'domain', 'created_at')
    search_fields = ('name', 'email', 'phone', 'domain')
    ordering = ('-created_at',)
    list_filter = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'email', 'phone', 'password', 'profile_picture', 'domain')
        }),
    )