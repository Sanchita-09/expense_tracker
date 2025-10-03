from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'description', 'amount', 'date', 'display_category', 'created_at')
    list_filter = ('type', 'category', 'user')
    search_fields = ('description', 'custom_category', 'user__username')
