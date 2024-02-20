from django.views.decorators.csrf import csrf_exempt
from expense_app.models import Expense, Category
import json
from django.http import JsonResponse
from . import validate_expense

@csrf_exempt
def create_expense(request, user_id, cat_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            message, status = validate_expense.validate_create_data(data, user_id, cat_id)
            return JsonResponse({"status": status, "message": message})
        except:
            return JsonResponse({"message": "Error occurred"})
    return JsonResponse({"status":400, "message":  "Invalid request method"})

def get_expenses(request, user_id):
    if request.method == "GET":
        message, status = validate_expense.validate_get_expenses_by_user(user_id)
        return JsonResponse({"status": status, "message": message})
    return JsonResponse({"status":400, "message":  "Invalid request method"})

def get_expenses_by_id(request, id):
    if request.method == "GET":
        message, status = validate_expense.validate_get_expenses_by_id(id)
        return JsonResponse({"status": status, "message": message})
    return JsonResponse({"status":400, "message":  "Invalid request method"})


@csrf_exempt
def delete_expense(request, id):
    if request.method == "DELETE":
        message, status = validate_expense.validate_delete_expense(id)
        return JsonResponse({"status": status,"message": message})
    return JsonResponse({"status":400, "message":  "Invalid request method"})


@csrf_exempt
def update_expense(request, id):
    if request.method == "PUT":
        data = json.loads(request.body)
        message, status = validate_expense.validate_update_expenses(data,id)
        return JsonResponse({"status": status, "message": message})
    return JsonResponse({"status":400, "message":  "Invalid request method"})
            
        