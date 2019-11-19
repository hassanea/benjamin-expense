from django.contrib import admin
from expenses.models import AccountPreferences, Expense

# Register your models here.
admin.site.register(AccountPreferences)
admin.site.register(Expense)