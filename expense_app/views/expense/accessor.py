from expense_app.models import Expense
from ..user import accessor as user_accessor
from ..category import accessor as category_accessor


def get_expense_by_id(id):
    data = Expense.objects.filter(id = id).values().first()
    return data

def get_expense_by_user(user_id):
    data = Expense.objects.filter(user = user_id).values().all()
    return list(data)

def create_expense(data, user_id, cat_id):
    user = user_accessor.get_user_by_id(user_id)
    category = category_accessor.get_category_by_id(cat_id)
    Expense.objects.create(user=user, expense_date=data["expense_date"], expenses= data["expenses"],note = data["note"],category=category)
    
def update_expense(data, id):
    expense = Expense.objects.filter(id = id).first()
    expense.expenses = data["expenses"]
    expense.expense_date = data["expense_date"]
    expense.note = data["note"]
    expense.save()
    