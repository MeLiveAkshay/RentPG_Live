# rentpg_live/admin__url.py

from django.urls import path
from rentpg_live.admin import admin__web

urlpatterns = [
    path('admin/', admin__web.admin_panel),
    path('admin/dashboard/', admin__web.admin_dashboard),
]
