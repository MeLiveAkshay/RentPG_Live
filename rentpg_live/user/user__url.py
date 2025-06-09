# rentpg_live/admin__url.py

from django.urls import path
from rentpg_live.user import user__web

urlpatterns = [
    path('user/login/', user__web.userLogin, name='user_login'),
    path('user/dashboard/', user__web.userDashboard, name='user_dashboard'),
    path('user/logout/', user__web.userLogout, name='user_logout'),
    path('user/register/', user__web.userRegister, name='register'),
]
