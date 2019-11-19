from datetime import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect

from .forms import AccountPreferencesForm, ExpenseCreationForm, ExpenseUserCreationForm
from .helpers import calculate_date_links, calculate_end_date, months
from .models import AccountPreferences, Expense

@login_required(redirect_field_name="accounts/login")
def index(request, year=datetime.today().year, month=datetime.today().month):
    if month == 0 | month > 12:
        return HttpResponseNotFound('<h1>Resource not found!<h1>')

    (prev_year, prev_month, next_year, next_month) = calculate_date_links(year, month)

    query = Expense.objects.filter(
        user = request.user
    ).filter(
        start_date__lt=datetime(next_year, next_month, 1)
    ).filter(
        end_date__gte=datetime(year, month, 1)
    ).order_by('start_date__day', 'start_date__year', 'start_date__month')

    month_sum = query.aggregate(Sum('value'))["value__sum"]
    if month_sum == None:
        month_sum = 0
        
    monthly_expense_limit = AccountPreferences.objects.filter(user=request.user)[0].monthly_expense_limit
    if monthly_expense_limit == None:
        monthly_expense_limit = "N/A"
        net_monthly_expense_margin = month_sum
    else:
        net_monthly_expense_margin = monthly_expense_limit - month_sum

    if net_monthly_expense_margin < 0: 
        net_monthly_expense_margin_color = "red"
    else:
        net_monthly_expense_margin_color = "forestgreen"

    args = {
        "expenses" : query,
        "prev_year" : prev_year,
        "prev_month" : prev_month,
        "next_year" : next_year,
        "next_month" : next_month,
        "pretty_month" : months[month],
        "pretty_year" : year,
        "month_sum" : month_sum,
        "monthly_expense_limit" : monthly_expense_limit,
        "net_monthly_expense_margin" : net_monthly_expense_margin,
        "net_monthly_expense_margin_color" : net_monthly_expense_margin_color
    }

    return render(request, 'expenses/index.html', args)

def signup(request):
    if request.method == 'POST':
        form = ExpenseUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = ExpenseUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(redirect_field_name="accounts/login")
def account_prefs(request):
    if request.method == 'POST':
        # parse the updated information and save it
        form = AccountPreferencesForm(request.POST, instance=request.user.accountpreferences)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AccountPreferencesForm(instance=request.user.accountpreferences)
    return render(request, 'registration/account_prefs.html', {'form': form})

@login_required(redirect_field_name="accounts/login")
def create_expense(request):
    if request.method == 'POST':
        form = ExpenseCreationForm(request.POST)
        if form.is_valid():
            # create an expense object and fill out its fields
            # using data entered in the form
            expense = Expense()
            expense.user = request.user
            expense.title = form.cleaned_data['title']
            expense.color = form.cleaned_data['color']
            expense.comment = form.cleaned_data['comment']
            expense.value = form.cleaned_data['value']
            expense.start_date = form.cleaned_data['start_date']
            expense.recurrences = form.cleaned_data['recurrences']
            expense.end_date = calculate_end_date(expense.start_date, expense.recurrences)
            print(expense.end_date)

            expense.save()
            return redirect('index')
    else:
        form = ExpenseCreationForm()
    return render(request, 'expenses/create-expense.html', {'form': form})

@login_required(redirect_field_name="accounts/login")
def delete_expense(request, expense_id):
    instance = get_object_or_404(Expense, pk=expense_id)
    instance.delete()
    return redirect('index')