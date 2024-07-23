"""
URL configuration for A2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views
from banks import views as banks_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.home, name='home'),  # Home view URL pattern
    path('accounts/register/', accounts_views.register, name='register'),
    path('accounts/login/', accounts_views.login_view, name='login'),
    path('accounts/logout/', accounts_views.logout_view, name='logout'),
    path('accounts/profile/view/', accounts_views.profile_view, name='profile_view'),
    path('accounts/profile/edit/', accounts_views.profile_edit, name='profile_edit'),
    path('banks/add/', banks_views.add_bank, name='add_bank'),
    path('banks/<int:bank_id>/branches/add/', banks_views.add_branch, name='add_branch'),
    path('banks/all/', banks_views.list_banks, name='list_banks'),  # Updated to list_banks view
    path('banks/<int:bank_id>/details/', banks_views.bank_details, name='bank_details'),
    path('banks/branch/<int:branch_id>/details/', banks_views.branch_details, name='branch_details'),
    path('banks/branch/<int:branch_id>/edit/', banks_views.edit_branch, name='edit_branch'),
]





