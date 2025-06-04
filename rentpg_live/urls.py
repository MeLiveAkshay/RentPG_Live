from django.contrib import admin
from django.urls import path
from rentpg_live import views
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

] 




