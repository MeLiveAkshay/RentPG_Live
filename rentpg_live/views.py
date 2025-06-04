from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data= {
        'title': 'Home - RentPG Live',
        'heading': 'Welcome to RentPG Live',
        'description': 'Find your perfect PG accommodation easily and quickly.',
        'authors': 'RentPG Live Team',
        'keywords': 'PG, accommodation, rent, live, housing',
        'features': [
            'Wide range of listings',
            'User-friendly interface',
            'Secure booking process'
        ]
    }
    return render(request, 'page/index.html')

def about(request):
    return render(request, 'page/about.html')

def contact(request):
    return render(request, 'page/contact.html')

def terms(request):
    return render(request, 'page/terms.html')