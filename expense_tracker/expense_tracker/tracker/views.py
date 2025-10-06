from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm
from django.contrib import messages
from django.db.models import Max, Min, Sum



# Home page
def home(request):
    return render(request, "tracker/base.html")


# Signup view
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tracker:login')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/signup.html', {'form': form})


# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('tracker:dashboard')
        else:
            # Add error message
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    
    return render(request, 'tracker/login.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect('tracker:login')

# Dashboard view
@login_required
def dashboard(request):
    # Filter transactions
    incomes = Transaction.objects.filter(user=request.user, type='income')
    expenses = Transaction.objects.filter(user=request.user, type='expense')

    # Aggregated values
    total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0
    max_income = incomes.aggregate(max=Max('amount'))['max'] or 0
    min_income = incomes.aggregate(min=Min('amount'))['min'] or 0

    total_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0
    max_expense = expenses.aggregate(max=Max('amount'))['max'] or 0
    min_expense = expenses.aggregate(min=Min('amount'))['min'] or 0

    net_income = total_income - total_expense

    context = {
        'incomes': incomes,
        'expenses': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'net_income': net_income,
        'max_income': max_income,
        'min_income': min_income,
        'max_expense': max_expense,
        'min_expense': min_expense,
    }
    return render(request, 'tracker/dashboard.html', context)

#Add income view
@login_required
def add_income(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.type = 'income'
            income.save()
            return redirect('tracker:dashboard')
    else:
        form = TransactionForm()
    return render(request, 'tracker/add_income.html', {'form': form})

# Add expense view
@login_required
def add_expense(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.type = 'expense'
            expense.save()
            return redirect('tracker:dashboard')
    else:
        form = TransactionForm()
    return render(request, 'tracker/add_expense.html', {'form': form})


# Income history view
@login_required
def income_history(request):
    incomes = Transaction.objects.filter(user=request.user, type='income')
    return render(request, 'tracker/history_income.html', {'incomes': incomes})


# Expense history view
@login_required
def expense_history(request):
    expenses = Transaction.objects.filter(user=request.user, type='expense')
    return render(request, 'tracker/history_expense.html', {'expenses': expenses})


# Edit income view
@login_required
def edit_income(request, pk):
    income = get_object_or_404(Transaction, pk=pk, user=request.user, type='income')
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('tracker:income_history')  # ✅ fixed
    else:
        form = TransactionForm(instance=income)
    return render(request, 'tracker/edit_income.html', {'form': form})


# Edit expense view
@login_required
def edit_expense(request, pk):
    expense = get_object_or_404(Transaction, pk=pk, user=request.user, type='expense')
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('tracker:expense_history')  # ✅ fixed
    else:
        form = TransactionForm(instance=expense)
    return render(request, 'tracker/edit_expense.html', {'form': form})


# Delete income view
@login_required
def delete_income(request, pk):
    print("Trying to delete income with pk:", pk, "for user:", request.user)
    income = get_object_or_404(Transaction, pk=pk, user=request.user, type='income')
    income.delete()
    return redirect('tracker:income_history')



# Delete expense view
@login_required
def delete_expense(request, pk):
    print("Trying to delete income with pk:", pk, "for user:", request.user)
    expense = get_object_or_404(Transaction, pk=pk, user=request.user, type='expense')
    expense.delete()
    return redirect('tracker:expense_history')


