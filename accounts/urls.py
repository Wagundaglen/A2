from django.urls import path
from .views import register, login_view, logout_view, view_profile, edit_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/view/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]

