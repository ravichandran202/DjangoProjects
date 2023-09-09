from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("",views.chat,name='chat'),
    path("/delete/<int:id>",views.chatdelete,name='chatdelete'),
]