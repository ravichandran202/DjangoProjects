from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import requests
from .models import History
from django.contrib.auth import authenticate
from django.conf import settings
from django.core.mail import send_mail


def weatherInfo(city="Mysore"):
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q": city, "days": "1"}

    headers = {
        "X-RapidAPI-Key": "65ad8e523fmshe2887d22f78c6a6p11a1ebjsnca2cd0a010af",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        return response.json()
    except:
        response = requests.get(url, headers=headers, params={
                                "q": 'Mysore', "days": "1"})
        return response.json()


def aboutLocation(place="Mysore"):
    url = "https://lemurbot.p.rapidapi.com/chat"

    payload = {
        "bot": "doc-bot",
        "client": "d531e3bd-b6c3-4f3f-bb58-a6632cbed5e2",
        "message": f"tell me about {place}"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "53a9b3afa9mshaf64aae96218a40p1799f9jsn138763ecaff7",
        "X-RapidAPI-Host": "lemurbot.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers).json()
    return str(response['data']['conversation']['output'])[:400]


def indexPage(request):
    weather = []
    location = "Mysore"
    weather = weatherInfo()
    about_place = aboutLocation()

    if request.method == 'POST':
        location = request.POST['location']
        weather = weatherInfo(location)
        about_place = aboutLocation(location)
        if request.user.is_authenticated:
            temperature = weather['current']['temp_c']
            created = weather['location']['localtime']
            History(host=request.user, location=location,
                    temperature=temperature, created=created).save()

    return render(request, "weatherapp/index.html", {
        "weather": weather,
        "max_temp": weather['forecast']['forecastday'][0]['day']['maxtemp_c'],
        "min_temp": weather['forecast']['forecastday'][0]['day']['mintemp_c'],
        "avg_temp": weather['forecast']['forecastday'][0]['day']['avgtemp_c'],
        "hourly_temp": weather['forecast']['forecastday'][0]['hour'],
        "about_place": about_place
    })


def login(request):
    if request.method == 'POST':
        username = request.POST['login-username']
        password = request.POST['login-password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("weatherapp:indexPage")
        else:
            messages.info(request, 'username or Password is incorrect')
            return redirect("weatherapp:login")

    return render(request, "weatherapp/login.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['signup-username']
        email = request.POST['signup-email']
        password = request.POST['signup-password1']
        password2 = request.POST['signup-password2']

        if password2 == password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists")
                return redirect('weatherapp:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "username Already Exists")
                return redirect('weatherapp:signup')
            else:
                user = User.objects.create_user(username, email, password)
                user.save()
                welcomeEmailSender(username,email)
                return redirect('weatherapp:login')
        else:
            messages.info(request, "Please Enter same Password")
            return redirect('weatherapp:signup')

    return render(request, "weatherapp/signup.html")


def logout(request):
    auth.logout(request)
    return redirect('login')


def history(request):
    historyEmailSender(request)
    return render(request, "weatherapp/history.html", {
        "histories": History.objects.filter(host=request.user)[::-1]
    })


def welcomeEmailSender(username,email):
    subject = 'Thank You for Registering with Us!'
    message = f"Hello {username},\nThank You for Joining! Welcome to Weather App.\nStay prepared and informed with our weather updates\n\nRegards,\nThe WeatherApp."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list)
    
def historyEmailSender(request):
    subject = 'Your Weather Search History'
    start_message = f"Hello {request.user.username},\nWe're glad you're enjoying our Weather App! Here's a quick recap of your recent weather searches:"
    operation_message = ""
    end_message = "\nKeep exploring and stay weather-ready!\n\nRegards,\nThe WeatherApp."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email, ]
    
    records = History.objects.filter(host=request.user)
    if records:
        count = 0
        operation_message += "\n\n----------HISTORY----------\n\n"
        for record in records:
            count += 1
            operation_message += f"\n----------Record - {count}----------"
            operation_message += f"\nPlace : {record.location}\nTemp : {record.temperature}\nTime : {record.created}\n\n"
    else:
        operation_message += "\n\n----NO RECORDS FOUND----\n\n"
    
    final_message = start_message+operation_message+end_message
    
    send_mail(subject, final_message, email_from, recipient_list)
