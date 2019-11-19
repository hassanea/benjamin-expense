from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from expenses.models import Expense

from .models import AccountPreferences

class ExpenseUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=36, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=36, required=False, help_text='Optional')
    email = forms.EmailField(max_length=256, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ExpenseCreationForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'color', 'comment', 'value', 'start_date', 'recurrences')
        widgets = {
            'start_date' : forms.DateInput(attrs={'type': 'date'}),
        }

class AccountPreferencesForm(forms.ModelForm):
    class Meta:
        model = AccountPreferences
        fields = ('monthly_expense_limit',)