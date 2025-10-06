from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['description', 'amount', 'date', 'category', 'custom_category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.TextInput(attrs={'placeholder': 'Enter description'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter amount'}),
            'category': forms.Select(attrs={'id': 'category-select'}),
            'custom_category': forms.TextInput(attrs={'placeholder': 'Enter custom category', 'style': 'display:none;', 'id': 'custom-category-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initially hide custom_category field if category is not Other
        if self.instance and self.instance.category != "Other":
            self.fields['custom_category'].widget.attrs['style'] = 'display:none;'



