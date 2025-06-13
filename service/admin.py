from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from service.models import User, ExampleModel
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'present_address', 'profession', 'created_at')
    search_fields = ('name', 'email', 'phone_number')

# Register your models here.
@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon', 'created_at')
    search_fields = ('name', 'description')
admin.site.site_header = "RentPG Admin"
admin.site.site_title = "RentPG Admin Portal"