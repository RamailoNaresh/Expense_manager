from expense_app.models import Category
from ..user import accessor as user_accessor

def get_category_by_id(id):
    category = Category.objects.get(id = id)
    return category

def get_category_by_id_display(id):
    category = Category.objects.filter(id = id).values().first()
    return category

def get_category_by_user(user_id):
    user = user_accessor.get_user_by_id(user_id)
    categories = Category.objects.filter(user = user).values().all()
    return list(categories)


def create_category(data, user_id):
    user =user_accessor.get_user_by_id(user_id)
    Category.objects.create(name = data["name"].capitalize(), budget = data["budget"], user = user)
    
def update_category(data, id):
    category = Category.objects.filter(id = id).first()
    category.name = data["name"].capitalize()
    category.budget = data["budget"]
    category.save()
    

    