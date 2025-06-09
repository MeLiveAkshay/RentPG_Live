# rentpg_live/admin__web.py

from django.http import HttpResponse

def admin_panel(request):
    return HttpResponse("Admin Panel")
