from django.contrib import admin
from .models import AdminMemberModel, OurTeam

@admin.register(AdminMemberModel)
class AdminMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'created_at')
    search_fields = ('name', 'email', 'role')
    ordering = ('-created_at',)
    list_filter = ('created_at',)

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'created_at', 'github_link', 'linkedin_link')
    search_fields = ('name', 'position')
    ordering = ('-created_at',)
    list_filter = ('created_at',)
