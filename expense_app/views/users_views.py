from django.shortcuts import render
from expense_app.models import UserProfile
from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

def get_user(request):
    datas = User.objects.all()
    json_data = list(datas.values())
    return JsonResponse({"data": json_data})

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data["username"]
            email = data["email"]
            password = data["password"]
            if username == "" or email == "" or password == "":
                return JsonResponse({"error": "Fields cannot be empty"}, status = 400)
            user = User.objects.filter(username = username).first()
            if user:
                return JsonResponse({"error": "Email already exists"})
            user1 = User.objects.create(username = username, email = email, password = make_password(password))
            return JsonResponse({"message": "User created successfully", "data": data})
        except:
            return JsonResponse({"message": "Error occurred"})
    return JsonResponse({"message": "Invalid request method"})


def get_user_by_id(request, id):
    user = User.objects.filter(id = id).values().first()
    if user:
        profile = UserProfile.objects.filter(user = user["id"]).values().first()
        return JsonResponse({"data": user, "profile": profile})
    else:
        return JsonResponse({"message": "User doesn't exist"})
 
@csrf_exempt   
def delete_user(request, id):
    if request.method == "DELETE":
        user = User.objects.filter(id = id).first()
        if user:
            json_data = {
                "name": user.username,
                "email": user.email
            }
            user.delete()
            return JsonResponse({"message": "User successfully deleted", "data": json_data})
        else:
            return JsonResponse({"message": "User doesn't exist"})
    return JsonResponse({"message": "Invalid request method"})
    
@csrf_exempt
def update_user(request, id):
    if request.method == "PUT":
        user = User.objects.filter(id = id).first()
        if user:
            try:
                data = json.loads(request.body)
                user1 = User.objects.exclude(id=user.id).filter(email=data["email"]).first()
                if user1:
                    return JsonResponse({"message": "User already exist with give email"})
                user.username = data["username"]
                user.email = data["email"]
                user.password = make_password(data["password"])
                user.save()
                json_data = {
                    "name": user.username,
                    "email": user.email,
                    "password": user.password
                }
                return JsonResponse({"message": "User data successfully updated","data": json_data})
            except:
                return JsonResponse({"message": "Error occurred"})
        return JsonResponse({"message": "User doesn't exist"})
    return JsonResponse({"message": "Invalid request method"})


    
@csrf_exempt
def create_user_profile(request, id):
    if request.method == "POST":
        user = User.objects.filter(id = id).first()
        if user:
            try:
                data = json.loads(request.body)
                number = data["number"]
                address = data["address"]
                income_month = data["income_month"]
                if number == "" or address == "" or income_month == "":
                    return JsonResponse({"message": "Fields cannot be empty"})
                userprofile = UserProfile.objects.create(number= number, address= address, income_month = income_month, user= user)
                return JsonResponse({"message": "user profile created"})
            except:
                return JsonResponse({"message": "Error occurred"})
        return JsonResponse({"message": "User doesn;t exist"})
    return JsonResponse({"message": "Invalid request method"})


@csrf_exempt
def update_profile(request, id):
    if request.method == "PUT":
        user = User.objects.filter(id  = id).first()
        if user:
            profile = UserProfile.objects.filter(user= user).first()
            try:
                data = json.loads(request.body)
                if profile:
                    profile.number = data["number"]
                    profile.address = data["address"]
                    profile.income_month = data["income_month"]
                    profile.save()
                    return JsonResponse({"message": "SUccessfully updated"})
                return JsonResponse({"message":"Profile doesn't exists"})
            except:
                return JsonResponse({"message": "Error occurred"})
        return JsonResponse({"message":"User doesn't exists"})
    return JsonResponse({"message": "Invalid request method"})