from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .models import Bank, Branch
from .forms import BankForm, BranchForm

@login_required
def add_bank(request):
    """
    Handle the creation of a new bank.
    """
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            bank = form.save(commit=False)
            bank.owner = request.user  # Associate the bank with the current user
            bank.save()
            return redirect(reverse('bank_details', args=[bank.id]))
    else:
        form = BankForm()
    
    return render(request, 'banks/add_bank.html', {'form': form})

@login_required
def add_branch(request, bank_id):
    """
    Handle the creation of a new branch for a specific bank.
    """
    bank = get_object_or_404(Bank, id=bank_id)
    if bank.owner != request.user:
        return HttpResponse(status=403)  # Forbidden access if the user is not the owner
    
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.bank = bank  # Associate the branch with the selected bank
            branch.save()
            return redirect(reverse('branch_details', args=[branch.id]))
    else:
        form = BranchForm()
    
    return render(request, 'banks/add_branch.html', {'form': form, 'bank': bank})

def list_banks(request):
    """
    Display a list of all banks.
    """
    banks = Bank.objects.all()
    return render(request, 'banks/list_banks.html', {'banks': banks})

def bank_details(request, bank_id):
    """
    Display details for a specific bank, including its branches.
    """
    bank = get_object_or_404(Bank, id=bank_id)
    branches = bank.branches.all()  # Retrieve all branches related to the bank
    return render(request, 'banks/bank_details.html', {'bank': bank, 'branches': branches})

def branch_details(request, branch_id):
    """
    Provide JSON data for a specific branch.
    """
    branch = get_object_or_404(Branch, id=branch_id)
    branch_data = {
        'id': branch.id,
        'name': branch.name,
        'transit_number': branch.transit_number,
        'address': branch.address,
        'email': branch.email,
        'capacity': branch.capacity,
        'last_modified': branch.last_modified,
        'bank': branch.bank.name,
    }
    return JsonResponse(branch_data)

@login_required
def edit_branch(request, branch_id):
    """
    Handle the editing of an existing branch.
    """
    branch = get_object_or_404(Branch, id=branch_id)
    if branch.bank.owner != request.user:
        return HttpResponse(status=403)  # Forbidden access if the user is not the owner

    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect(reverse('branch_details', args=[branch.id]))
    else:
        form = BranchForm(instance=branch)
    
    return render(request, 'banks/edit_branch.html', {'form': form, 'branch': branch})

@login_required
def edit_bank(request, bank_id):
    """
    Handle the editing of an existing bank.
    """
    bank = get_object_or_404(Bank, id=bank_id)
    if bank.owner != request.user:
        return HttpResponse(status=403)  # Forbidden access if the user is not the owner

    if request.method == 'POST':
        form = BankForm(request.POST, instance=bank)
        if form.is_valid():
            form.save()
            return redirect(reverse('bank_details', args=[bank.id]))
    else:
        form = BankForm(instance=bank)
    
    return render(request, 'banks/edit_bank.html', {'form': form, 'bank': bank})
