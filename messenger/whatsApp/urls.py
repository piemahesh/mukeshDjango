from django.urls import path
from . import views

urlpatterns = [
    path("",views.homePage,name="login"),
    path("about/",views.aboutPage,name="aboutPage"),
    path("register/",views.register,name="register"),
    path("view/",views.viewPage,name="view"),
    path("addUser/",views.addUser,name="addUser"),
    path("viewUser/",views.viewUser,name="viewUser"),
    path("logout/", views.logout, name="logout")
]
