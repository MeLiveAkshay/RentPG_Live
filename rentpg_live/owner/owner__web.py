# rentpg_live/admin__web.py

from django.http import HttpResponse
from django.shortcuts import render

def owner_panel(request):
    return HttpResponse("owner Panel")

# This is a placeholder for the owner panel view.
def owner_dashboard(request):
    return render(request, 'owner/owner_dashboard.html')

def owner_login(request):
    return render(request, 'owner/owner_login.html')