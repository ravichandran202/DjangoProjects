from django.urls import path
from . import views

app_name = "weatherapp"

urlpatterns = [
    path("",views.indexPage,name="indexPage"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("logout",views.logout,name="logout"),
    path("history",views.history,name="history"),
]
