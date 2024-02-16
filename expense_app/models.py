from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    profile_img = models.ImageField(upload_to = "profile/")
    address = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100)
    

class Expense(models.Model):
    expenses = models.PositiveIntegerField()
    expense_date =models.DateField()
    note = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    