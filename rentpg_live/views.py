from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
    meta_data = {
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

    # Example data for available rooms
    base_room = {
        'image_url': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=800&q=60',
        'facility': 'WiFi, AC, Attached Bathroom',
        'hotel_name': 'Green Stay',
        'hotel_description': 'A comfortable room with modern amenities.',
        'location': 'Delhi',
        'price': 8500
    }

    rooms = []
    for i in range(1, 26):
        room = base_room.copy()
        room['id'] = i
        room['name'] = f'Demo Room {i}'
        room['price'] += i * 100
        rooms.append(room)

    context = {
        **meta_data,
        'rooms': rooms
    }

    return render(request, 'page/index.html', context)

def about(request):
    return render(request, 'page/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Here you can handle the form submission, e.g., save to DB or send an email

        return render(request, 'page/contact.html', {
            'success': True,
            'name': name,
            'email': email,
            'message': message
        })
    return render(request, 'page/contact.html')

def terms(request):
    return render(request, 'page/terms.html')


def careers(request):
    data={
        'title': 'Careers - RentPG Live',
        'heading': 'Join Our Team',
        'description': 'Explore exciting career opportunities with RentPG Live.',
        'authors': 'RentPG Live Team',
        'keywords': 'careers, jobs, rentpg live, employment'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        position = request.POST.get('position')
        resume = request.FILES.get('resume')

        # TODO: Save application info to DB or send email notification here

        return render(request, 'page/careers.html',data, {
            'success': True,
            'name': name,
            'position': position,
            'phone': phone,
            'email': email,
        })
    
    return render(request, 'page/careers.html')


def footer(request):
    data = {
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


# Add this in views.py

def room_detail(request, room_id):
    # Example static data; you can fetch from a database instead
    room = {
        'id': room_id,
        'name': f'Demo Room {room_id}',
        'image_url': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=800&q=60',
        'facility': 'WiFi, AC, Attached Bathroom',
        'hotel_name': 'Green Stay',
        'hotel_description': 'A comfortable room with modern amenities.',
        'location': 'Delhi',
        'price': 8500 + room_id * 100
    }
    return render(request, 'element/room_detail.html', {'room': room})
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def book_room(request, room_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        move_in_date = request.POST.get('move_in_date')
        
        # Optionally save to DB or send email here

        return render(request, 'element/booking_confirmation.html', {
            'room_id': room_id,
            'name': name,
            'email': email,
            'phone': phone,
            'move_in_date': move_in_date
        })

    return HttpResponse("Invalid request method.", status=400)
