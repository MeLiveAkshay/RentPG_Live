
from django.contrib import admin
from django.urls import path
from rentpg_live import views

urlpatterns = [
    path('cp-admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('footer/', views.footer, name='footer'),
    path('userAdmin/', views.userAdmin, name='userAdmin'),
]
