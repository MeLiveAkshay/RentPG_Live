from django.shortcuts import render
def availableroom(request):
    base_room = {
        'image_url': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=800&q=60',
        'facility': 'WiFi, AC, Attached Bathroom',
        'hotel_name': 'Green Stay',
        'hotel_description': 'A comfortable room with modern amenities.',
        'location': 'Delhi',
        'price': 8500
    }

    data = []
    for i in range(1, 26):
        room = base_room.copy()
        room['id'] = i
        room['name'] = f'Demo Room {i}'
        room['price'] += i * 100
        data.append(room)

    return render(request, 'element/availableRoom.html', {'rooms': data})
