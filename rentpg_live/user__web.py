from django.shortcuts import render
from django.http import HttpResponse
def userLogin(request):
    return render(request, 'user/user_login.html')