from . import accessor
import os
from expense_app.models import CustomUser


def validate_create_data(data):
    try:
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        number = data.get("number")
        address = data.get("address")
        country = data.get("country")
        if username == "" or email == "" or password == "" or address == "" or country == "" or number == "":
            return "All fields are required", 400
        user = CustomUser.objects.filter(email = email).first()
        if user:
            return "Email already exists", 400
        accessor.create_user(data)
        return "Successfully created", 200
    except:
        return "Error occurred", 400

def validate_get_user_by_id(id):
    user = accessor.get_user_by_id_display(id)
    if user:
        return user, 200
    return "User doesn't exists", 400

def validate_delete_user( id):
    user = accessor.get_user_by_id(id)
    if user:
        user.delete()
        return "User deleted successfully", 200
    else:
        return "User doesn;t exists", 400
    
    
def validate_update_user(data,id):
    try:
        user1 = CustomUser.objects.exclude(id=id).filter(email=data["email"]).first()
        if user1:
            return "Email already exists", 400
        
        user = accessor.get_user_by_id(id)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        number = data.get("number")
        address = data.get("address")
        country = data.get("country")
        if username == "" or email == "" or password == "" or address == "" or country == "" or number == "":
            return "All fields are required", 400
        if user != None:
            accessor.update_user(data, id)
            return "Successfully updated", 200
        return "User doesn't exists", 400
    except:
        return "Error occurred", 400
    
    

