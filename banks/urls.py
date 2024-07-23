from django.urls import path
from .views import add_bank, add_branch, list_banks, bank_details, branch_details, edit_branch

urlpatterns = [
    path('add/', add_bank, name='add_bank'),
    path('<int:bank_id>/branch/add/', add_branch, name='add_branch'),
    path('', list_banks, name='list_banks'),
    path('<int:bank_id>/details/', bank_details, name='bank_details'),
    path('branch/<int:branch_id>/details/', branch_details, name='branch_details'),
    path('branch/<int:branch_id>/edit/', edit_branch, name='edit_branch'),
]

