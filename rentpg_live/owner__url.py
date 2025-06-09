# rentpg_live/admin__url.py

from django.urls import path
from rentpg_live import owner__web

urlpatterns = [
    path('owner/', owner__web.owner_panel),
]
