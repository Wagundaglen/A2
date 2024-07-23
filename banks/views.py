from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .models import Bank, Branch
from .forms import BankForm, BranchForm

@login_required
def add_bank(request):
    """
    Handle adding a new bank.
    """
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            bank = form.save(commit=False)
            bank.owner = request.user
            bank.save()
            return redirect(f'/banks/{bank.id}/details/')
    else:
        form = BankForm()
    return render(request, 'banks/add_bank.html', {'form': form})

@login_required
def add_branch(request, bank_id):
    """
    Handle adding a new branch to a specific bank.
    """
    bank = get_object_or_404(Bank, id=bank_id)
    if bank.owner != request.user:
        return HttpResponse(status=403)
    
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.bank = bank
            branch.save()
            return redirect(f'/banks/branch/{branch.id}/details/')
    else:
        form = BranchForm(initial={'email': 'admin@utoronto.ca'})
    return render(request, 'banks/add_branch.html', {'form': form})

def list_banks(request):
    """
    List all banks.
    """
    banks = Bank.objects.all()
    return render(request, 'banks/list_banks.html', {'banks': banks})

def bank_details(request, bank_id):
    """
    Display details for a specific bank, including its branches.
    """
    bank = get_object_or_404(Bank, id=bank_id)
    branches = bank.branches.all()
    return render(request, 'banks/bank_details.html', {'bank': bank, 'branches': branches})

def branch_details(request, branch_id):
    """
    Return JSON data for a specific branch.
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
    Handle editing an existing branch.
    """
    branch = get_object_or_404(Branch, id=branch_id)
    if branch.bank.owner != request.user:
        return HttpResponse(status=403)

    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect(f'/banks/branch/{branch.id}/details/')
    else:
        form = BranchForm(instance=branch)
    return render(request, 'banks/edit_branch.html', {'form': form})


