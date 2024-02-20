from . import accessor
from ..category import accessor as category_accessor
from ..user import accessor as user_accessor
from expense_app.models import Expense

def validate_create_data(data, user_id, cat_id):
    try:
        expenses = data["expenses"]
        expense_date = data["expense_date"]
        note = data["note"]
        user = user_accessor.get_user_by_id(user_id)
        cat = category_accessor.get_category_by_id(cat_id)
        if user:
            if cat:
                if expense_date == "" or expenses == "":
                    return "Fields cannot be empty", 400
                accessor.create_expense(data, user_id, cat_id)
                return "Expense successfully created", 200
            return "Category doesn't exists", 400
        return "User doesn't exists", 400
    except:
        return "Error occurred", 400
    
    
    
def validate_get_expenses_by_user(user_id):
    try:
        user = user_accessor.get_user_by_id(user_id)
        if not user:
            return "User doesn't exists", 400
        data = accessor.get_expense_by_user(user_id)
        if data:
            return data, 200
        return "No data available", 400
    except:
        return "Error occurred", 400
    
def validate_get_expenses_by_id(id):
    try:
        data = accessor.get_expense_by_id(id)
        if data:
            return data, 200
        return "No data available", 400
    except:
        return "Error occurred",400
    
def validate_delete_expense(id):
    try:
        data = Expense.objects.filter(id = id).first()
        if data:
            data.delete()
            return "Data successfully deleted", 200
        return "No data available", 400
    except:
        return "Error occurred", 400
    
    
def validate_update_expenses(data,id):
    try:
        expense = accessor.get_expense_by_id(id)
        if not expense:
            return "Data doesn't exiists", 400
        expenses = data["expenses"]
        expense_date = data["expense_date"]
        note = data["note"]
        if expense_date == "" or expenses == "":
            return "Fields cannot be empty", 400
        accessor.update_expense(data, id)
        return "Expense successfully updated", 200
    except:
        return "Error occurred", 400