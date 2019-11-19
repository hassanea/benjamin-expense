from django.urls import include, path

import expenses.views as v

urlpatterns = [
    path('', v.index, name='index'),
    path('<int:year>/<int:month>/', v.index, name='view-month'),
    path('accounts/signup/', v.signup, name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/account-prefs', v.account_prefs, name="account-prefs"),
    path('create-expense/', v.create_expense, name="create-expense"),
    path('delete-expense/<int:expense_id>', v.delete_expense, name="delete-expense")
]