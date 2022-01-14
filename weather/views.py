import requests

from django.shortcuts import render
from django.http import HttpResponse
from .models import City
from .forms import weatherForms


# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2cae3b1f569a511945d2d91aa1288824'

    if request.method == 'POST':
        form = weatherForms(request.POST)
        form.save()

    form = weatherForms()

    weather_data = []

    cities = City.objects.all()

    for city in cities:

        r = requests.get(url.format(city)).json()
        print(r)
        city_weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)
    print(weather_data)

    context = {'weather_data' : weather_data, 'form' : form}

    print(context)

    return render(request, 'weather/weather.html', context)