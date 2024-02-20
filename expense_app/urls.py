from django.urls import path
from .views.category import category_views
from .views.expense import expense_views
from .views.user import users_views


urlpatterns = [
    path("create_user/", users_views.create_user, name = "create-user"),
    path("get_users/", users_views.get_user, name = "get-users"),
    path("get_user_by_id/<int:id>/", users_views.get_user_by_id, name = "user-id"),
    path("delete_user/<int:id>/", users_views.delete_user, name = "delete-user"),
    path("update_user/<int:id>/", users_views.update_user, name = "update-user"),
    path("create_category/<int:user_id>/", category_views.create_category, name = 'create-category'),
    path("get_categories_by_user/<int:id>/", category_views.get_categories_by_user, name = "categories"),
    path("get_categories_by_id/<int:id>/", category_views.get_category_by_id, name = 'category-id'),
    path("delete_category/<int:id>/", category_views.delete_category, name = "delete-category"),
    path("update_category/<int:id>/", category_views.update_category, name = "update-category"),
    path("create_expense/<int:user_id>/<int:cat_id>/", expense_views.create_expense, name = 'create-expense'),
    path("get_expenses/<int:user_id>/", expense_views.get_expenses, name = "expenses"),
    path("get_expense_by_id/<int:id>/", expense_views.get_expenses_by_id, name = "expense_by_id"),
    path("delete_expense/<int:id>/", expense_views.delete_expense, name = "delete-expense"),
    path("update_expense/<int:id>/", expense_views.update_expense, name = "update-expense"),
]