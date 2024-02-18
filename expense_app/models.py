from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class UserProfile(models.Model):
    number = models.PositiveIntegerField(validators = [MaxValueValidator(999999999)], null = True)
    address = models.CharField(max_length=100)
    income_month = models.PositiveIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100)
    

class Expense(models.Model):
    expenses = models.PositiveIntegerField()
    expense_date =models.DateField()
    note = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    