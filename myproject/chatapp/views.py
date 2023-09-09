from django.shortcuts import render
from datetime import datetime
from .models import Chat
# Create your views here.
def chat(request):
    if request.method == 'POST':
        text = request.POST['text']
        time = datetime.now().strftime("%d-%m-%Y  %I:%M %p")
        Chat(text=text,time=time).save()
    return render(request,'chat/chat.html',{
        'chats':Chat.objects.all()
    })
    
def chatdelete(request,id):
    Chat.objects.filter(id=id).delete()
    return render(request,'chat/chat.html',{
        'chats':Chat.objects.all()
    })