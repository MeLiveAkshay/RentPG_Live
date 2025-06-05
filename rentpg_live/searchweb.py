from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
import datetime

def search(request):
    query = request.GET.get('q', '').strip()

    # Dynamically generate 20 room items
    query_base_room = []
    for i in range(1, 21):
        query_base_room.append({
            'id': i,
            'room_id': i,
            'room_name': f'Demo Room {i}',
            'name': f'Demo Room {i}',
            'image_url': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=800&q=60',
            'facility': 'WiFi, AC, TV, Pool' if i % 2 == 0 else 'WiFi, AC, Heater',
            'hotel_name': f'Hotel {chr(64 + i)}',
            'hotel_description': 'A comfortable stay with great service.',
            'location': query,
            'price': 1000 + i * 100
        })

    return render(request, 'page/search_results.html', {
        'query': query,
        'rooms': query_base_room
    })

def search_room(request, room_id):
    # Generate dummy room detail based on room_id
    room_detail = {
        'room_id': room_id,
        'room_name': f'Demo Room {room_id}',
        'image_url': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=800&q=60',
        'facility': 'WiFi, AC, TV, Pool' if room_id % 2 == 0 else 'WiFi, AC, Heater',
        'hotel_name': f'Hotel {chr(64 + room_id)}',
        'hotel_description': 'A comfortable stay with great service.',
        'location': 'Unknown',  # or any default value
        'price': 1000 + room_id * 100
    }

    return render(request, 'page/search_room_detail.html', {
        'room': room_detail
    })

@csrf_exempt  # Only if needed — consider removing if not necessary
def book_room(request, room_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        move_in_date = request.POST.get('move_in_date')

        # Basic validation (optional)
        if not all([name, email, phone, move_in_date]):
            return HttpResponseBadRequest("Missing required booking details.")

        booking_id = f'BOOK-{room_id}-{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}'

        # Here you can save booking info to DB or send confirmation email

        return render(request, 'element/booking_confirmation.html', {
            'room_id': room_id,
            'name': name,
            'email': email,
            'phone': phone,
            'move_in_date': move_in_date,
            'booking_id': booking_id
        })

    return HttpResponseBadRequest("Invalid request method.")
