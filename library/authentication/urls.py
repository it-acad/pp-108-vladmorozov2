from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("home/", views.home, name="home"),
    path("users/", views.list_users, name="admin_list_users"),
    path("users/<int:user_id>/", views.view_user, name="admin_view_user"),
]
