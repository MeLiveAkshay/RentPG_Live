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
    return render(request, 'page/index.html', data)

def about(request):
    return render(request, 'page/about.html')

def contact(request):
    return render(request, 'page/contact.html')

def terms(request):
    return render(request, 'page/terms.html')


def footer(request):
    data={
        'version_no': '1.0.0',
        'version_name': 'Ram',
        'copyright': '© 2025 RentPG Live',
        'company_name': 'RentPG Live Pvt. Ltd.',
        'company_address': '123 RentPG Lane, City, Country',
        'company_email': 'contact@rentpg.com',
        'company_phone': '+1234567890'
    }
    return render(request, 'element/footer.html', data)

def userAdmin(request):
    data = {
        'title': 'User Admin - RentPG Live',
        'heading': 'User Administration',
        'description': 'Manage user accounts and settings.',
        'authors': 'RentPG Live Team',
        'keywords': 'user, admin, management, settings'
    }
    return render(request, 'element/userAdmin.html', data)