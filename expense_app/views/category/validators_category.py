from . import accessor
from expense_app.models import Category, CustomUser
from ..user import accessor as user_accessor



def validate_create_data(data, user_id):
    try:
        name = data["name"]
        budget = data["budget"]
        if name == "" or budget == "":
            return "Fields cannot be empty", 400
        user = user_accessor.get_user_by_id(user_id)
        check_cat = Category.objects.filter(name = name.capitalize(), user =user).first()
        if check_cat:
            return "Category already exists", 400
        accessor.create_category(data, user_id)
        return "Category Successfully created", 200
    except:
        return "Error occurred", 400
    
    
def validate_get_category_by_user(id):
    data = accessor.get_category_by_user(id)
    if data:
        return data, 200
    return "Data doesn't found", 400

def validate_get_category_by_id(id):
    data = accessor.get_category_by_id_display(id)
    if data:
        return data, 200
    return "Data doesn't found", 400

def validate_delete_category(id):
    data = accessor.get_category_by_id(id)
    if data:
        data.delete()
        return "Data succesfully deleted", 200
    return "Data doesn't exists", 400

def validate_update_category(data,id):
    try:
        name = data["name"]
        budget = data["budget"]
        if name == "" or budget == "":
            return "Fields cannot be empty", 400
        check_cat = accessor.get_category_by_id(id)
        if check_cat:
            accessor.update_category(data, id)
            return "Data successfully updated", 200
        return "Data doesn't exists", 400
    except:
        return "Error occurred", 400