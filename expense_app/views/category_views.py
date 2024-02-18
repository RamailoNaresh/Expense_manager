from django.views.decorators.csrf import csrf_exempt
from expense_app.models import Category
import json
from django.http import JsonResponse



@csrf_exempt
def create_category(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data["name"]
        category = Category.objects.filter(name = name).first()
        if category:
            return JsonResponse({"message": "category already exists"})
        cat_obj = Category.objects.create(name = name.capitalize())
        return JsonResponse({"message": "Category successfully created", "data": name})
    return JsonResponse({"message": "Error occurred"})


def get_categories(request):
    categories=  Category.objects.all().values()
    data = list(categories)
    return JsonResponse({"message":"Data received",  "data": data})

def get_category_by_id(request, id):
    cat = Category.objects.filter(id = id).values().first()
    if cat:
        return JsonResponse({"data": cat})
    return JsonResponse({"message": "Data doesn't exist"})

@csrf_exempt
def delete_category(request, id):
    if request.method == "DELETE":
        cat = Category.objects.filter(id = id).first()
        if cat:
            cat.delete()
            return JsonResponse({"message": "Data successfully deleted"})
        return JsonResponse({"message": "category doesn't exist"})
    return JsonResponse({"message": "Error occurred"})

@csrf_exempt
def update_category(request, id):
    if request.method == "PUT":
        cat = Category.objects.filter(id = id).first()
        if cat:
            data = json.loads(request.body)
            name = data["name"]
            cat_obj = Category.objects.filter(name = name.capitalize()).first()
            if cat_obj:
                return JsonResponse({"message": "category already exist"})
            cat.name = name.capitalize()
            cat.save()
            return JsonResponse({"message": "Category updated", "data": name})
        return JsonResponse({"message": "Category doesn't exist"})
    return JsonResponse({"message": "Error Occurred"})