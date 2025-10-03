from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TYPE_CHOICES = [
        ("income", "Income"),
        ("expense", "Expense"),
    ]

    CATEGORY_CHOICES = [
        # Income categories
        ("Salary", "Salary"),
        ("Business", "Business"),
        ("Gift", "Gift"),
        # Expense categories
        ("Food", "Food"),
        ("Travel", "Travel"),
        ("Shopping", "Shopping"),
        ("Bills", "Bills"),
        # Generic
        ("Other", "Other"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    custom_category = models.CharField(max_length=100, blank=True, null=True, help_text="Use if category is Other")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.description} - {self.amount}"

    @property
    def display_category(self):
        """Return custom category if set, else selected category"""
        return self.custom_category if self.category == "Other" and self.custom_category else self.category
