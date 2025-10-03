from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    # Add income / expense
    path('add_income/', views.add_income, name='add_income'),
    path('add_expense/', views.add_expense, name='add_expense'),

    # Income / Expense history
    path('income/history/', views.income_history, name='income_history'),
    path('expense/history/', views.expense_history, name='expense_history'),

    # Edit income / expense
    path('edit_income/<int:pk>/', views.edit_income, name='edit_income'),
    path('edit_expense/<int:pk>/', views.edit_expense, name='edit_expense'),

    # Delete income / expense
    path('delete_income/<int:pk>/', views.delete_income, name='delete_income'),
    path('delete_expense/<int:pk>/', views.delete_expense, name='delete_expense'),
]
