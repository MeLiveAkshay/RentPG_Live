# rentpg_live/admin__web.py

from django.http import HttpResponse
from django.shortcuts import render
# This is a placeholder for the admin panel view.

def admin_panel(request):
    return HttpResponse("Admin Panel")


# This is a placeholder for the admin panel view.
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')
