from expense_app.models import CustomUser
from django.contrib.auth.hashers import make_password


def create_user(data):
    CustomUser.objects.create(username = data["username"], email = data["email"], password = make_password(data["password"]), address=data["address"], number = data["number"], country=data["country"])
    

    
def get_user_by_id(id):
    user = CustomUser.objects.filter(id =id).first()
    return user

def get_user_by_id_display(id):
    user = CustomUser.objects.filter(id =id).values().first()
    return user


def get_users():
    users = CustomUser.objects.all().values()
    return list(users)


def update_user(data,id):
    user = get_user_by_id(id)
    user.username = data["username"]
    user.email = data["email"]
    user.password = make_password(data["password"])
    user.address = data["address"]
    user.country = data["country"]
    user.number = data["number"]
    user.save()
    
    