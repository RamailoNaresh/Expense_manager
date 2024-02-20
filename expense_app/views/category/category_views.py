from django.views.decorators.csrf import csrf_exempt
from expense_app.models import Category
import json
from django.http import JsonResponse
from . import validators_category


@csrf_exempt
def create_category(request, user_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            message, status = validators_category.validate_create_data(data, user_id)
            return JsonResponse({"status": status, "message": message})
        except:
            return JsonResponse({"message":"Error occurred"})
    return JsonResponse({"status": 400, "message": "Invalid request method"})


def get_categories_by_user(request, id):
    if request.method == "GET":
        message, status = validators_category.validate_get_category_by_user(id)
        return JsonResponse({"status": status, "message": message})
    return JsonResponse({"status": 400, "message": "Invalid request method"})

def get_category_by_id(request, id):
    if request.method == "GET":
        message, status = validators_category.validate_get_category_by_id(id)
        return JsonResponse({"status": status, "message": message})
    return JsonResponse({"status": 400, "message": "Invalid request method"})

@csrf_exempt
def delete_category(request, id):
    if request.method == "DELETE":
        message, status = validators_category.validate_delete_category(id)
        return JsonResponse({"status": status, "message": message})
    return JsonResponse({"status": 400, "message": "Invalid request method"})

@csrf_exempt
def update_category(request, id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            message, status = validators_category.validate_update_category(data,id)
            return JsonResponse({"status": status, "message": message})
        except:
            return JsonResponse({"message": "Error occurred"})
    return JsonResponse({"status": 400, "message": "Invalid request method"})