from django.urls import path
from userinfo import views

app_name= "userinfo"

urlpatterns= [
    path("", views.index, name="index"),
    path("register/", views.createuser, name="register"),
    path("login/", views.loginuser, name="login"),
    path("logout/", views.logoutuser, name="logout")
]