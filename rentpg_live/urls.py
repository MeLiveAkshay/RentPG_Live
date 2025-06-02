
from django.contrib import admin
from django.urls import path
from rentpg_live import views

urlpatterns = [
    path('cp-admin/', admin.site.urls),
    path('', views.index, name='index'),

]
