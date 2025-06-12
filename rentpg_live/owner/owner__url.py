# rentpg_live/admin__url.py

from django.urls import path
from rentpg_live.owner import owner__web

urlpatterns = [
    path('owner/', owner__web.owner_panel),
    path('owner/dashboard/', owner__web.owner_dashboard, name='owner_dashboard_view'),
    path('owner/login', owner__web.owner_login, name='owner_login')
]
