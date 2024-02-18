from django.views.decorators.csrf import csrf_exempt
from expense_app.models import Expense, Category
from django.contrib.auth.models import User
import json
from django.http import JsonResponse

@csrf_exempt
def create_expense(request, user_id, cat_id):
    if request.method == "POST":
        data = json.loads(request.body)
        expenses = data["expenses"]
        expense_date = data["expense_date"]
        note = data["note"]
        cat = Category.objects.filter(id = cat_id).first()
        user = User.objects.filter(id = user_id).first()
        if cat:
            if user:
                if expenses == "" or expense_date == "":
                    return JsonResponse({"message": "Expenses and expense_date is required"})
                expense = Expense.objects.create(expenses= expenses, expense_date=expense_date, note = note, user = user, category=cat)
                return JsonResponse({"message": "Expense added"})
            return JsonResponse({"message": "User doesn't exist"})
        return JsonResponse({"message": "category doesn't exist"})
    return JsonResponse({"message": "Error occurred"})

def get_expenses(request, user_id):
    user = User.objects.filter(id = user_id).first()
    if user:
        expenses = Expense.objects.filter(user = user).values().all()
        json_data = list(expenses)
        return JsonResponse({"message": "Data received", "data": json_data})
    return JsonResponse({"message": "User doesn't exists"})


def get_expenses_by_id(request, id):
    expense = Expense.objects.filter(id = id).values().first()
    if expense:
        return JsonResponse({"message": "Data received", "data": expense})
    return JsonResponse({"message": "Data doesn't exists"})

@csrf_exempt
def delete_expense(request, id):
    if request.method == "DELETE":
        expense = Expense.objects.filter(id = id).first()
        if expense:
            expense.delete()
            return JsonResponse({"message": "Data successfully deleted"})
        return JsonResponse({"message": "data doesn't exists"})
    return JsonResponse({"message": "Error occurred"})


@csrf_exempt
def update_expense(request, id):
    if request.method == "PUT":
        expense = Expense.objects.filter(id = id).first()
        if expense:
            data = json.loads(request.body)
            expense.expenses = data["expenses"]
            expense.expense_date = data["expense_date"]
            expense.note = data["note"]
            expense.save()
            return JsonResponse({"message": "Successfully updated"})
        return JsonResponse({"message": "Data doesn't exist"})
    return JsonResponse({"message": "Error occurred"})
            
        