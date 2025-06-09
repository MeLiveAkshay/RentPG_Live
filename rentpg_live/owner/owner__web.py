# rentpg_live/admin__web.py

from django.http import HttpResponse

def owner_panel(request):
    return HttpResponse("owner Panel")
