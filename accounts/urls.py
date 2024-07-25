# accounts/urls.py

from django.urls import path
from .views import register, login_view, logout_view, profile_view, profile_edit

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/view/', profile_view, name='profile_view'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]



