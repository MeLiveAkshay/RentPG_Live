from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'page/index.html')

def about(request):
    return render(request, 'page/about.html')

def contact(request):
    return render(request, 'page/contact.html')

def terms(request):
    return render(request, 'page/terms.html')