from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    address = models.CharField(max_length= 100)
    number =models.PositiveIntegerField(validators = [MaxValueValidator(9999999999)])
    country = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)
    budget = models.PositiveIntegerField(validators = [MaxValueValidator(999999)])
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)

class Expense(models.Model):
    expenses = models.PositiveIntegerField()
    expense_date =models.DateField()
    note = models.TextField(null = True, blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    