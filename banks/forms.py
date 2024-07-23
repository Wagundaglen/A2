from django import forms
from .models import Bank, Branch

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['name', 'address', 'phone_number']  # Ensure these fields are present in the Bank model

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'transit_number', 'address', 'email', 'capacity']


