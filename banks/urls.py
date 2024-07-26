from django.urls import path
from .views import add_bank, add_branch, list_banks, bank_details, branch_details, edit_branch, edit_bank

urlpatterns = [
    # Path to add a new bank
    path('add/', add_bank, name='add_bank'),
    
    # Path to add a branch to a specific bank
    path('<int:bank_id>/branch/add/', add_branch, name='add_branch'),
    
    # Path to list all banks
    path('', list_banks, name='list_banks'),
    
    # Path to view details of a specific bank
    path('<int:bank_id>/details/', bank_details, name='bank_details'),
    
    # Path to view details of a specific branch
    path('branch/<int:branch_id>/details/', branch_details, name='branch_details'),
    
    # Path to edit a specific branch
    path('branch/<int:branch_id>/edit/', edit_branch, name='edit_branch'),

    # Path to edit a specific bank
    path('<int:bank_id>/edit/', edit_bank, name='edit_bank'),  # Add this line
]


