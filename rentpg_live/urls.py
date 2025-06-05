from django.contrib import admin
from django.urls import path
from rentpg_live import views
from rentpg_live import searchweb
from rentpg_live import new__letter

from django.conf.urls.static import static
urlpatterns = [
    # Admin Panel
    path('cp-admin/', admin.site.urls),

    # Main Pages
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('footer/', views.footer, name='footer'),
    path('userAdmin/', views.userAdmin, name='userAdmin'),

    # Room Detail Page
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),
    
    # Booking Form Submission
    path('book-room/<int:room_id>/', views.book_room, name='book_room'),

    # Careers Page
    path('careers/', views.careers, name='careers'),



    # Search Functionality
    path('search/', searchweb.search, name='search_results'),
    path('room_search/<int:room_id>/', searchweb.search_room, name='search_room_detail'),
    path('search/book-room/<int:room_id>/', searchweb.book_room, name='book_room'),


    # Newsletter Subscription
    path('newsletter/', new__letter.newsletter, name='newsletter'),
    path('newsletter/thanks/', new__letter.newsletter_thanks, name='newsletter_thanks'),
    
] 




