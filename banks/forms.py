from django import forms
from .models import Bank, Branch

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['name', 'address', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter bank name'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter bank address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
        }
        labels = {
            'name': 'Bank Name',
            'address': 'Address',
            'phone_number': 'Phone Number',
        }
        help_texts = {
            'name': 'The name of the bank.',
            'address': 'The physical address of the bank.',
            'phone_number': 'Contact phone number of the bank.',
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Add validation for phone number format if needed
        return phone_number

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'transit_number', 'address', 'email', 'capacity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch name'}),
            'transit_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter transit number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter branch address'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch capacity'}),
        }
        labels = {
            'name': 'Branch Name',
            'transit_number': 'Transit Number',
            'address': 'Address',
            'email': 'Email Address',
            'capacity': 'Capacity',
        }
        help_texts = {
            'name': 'The name of the branch.',
            'transit_number': 'The transit number of the branch.',
            'address': 'The physical address of the branch.',
            'email': 'Contact email address of the branch.',
            'capacity': 'The maximum capacity of the branch.',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Additional email validation can be added here
        return email




