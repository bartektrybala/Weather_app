import requests
from django.shortcuts import render


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    api_key = '69238c44a6a9aee21feb1688f347b607'
    city = 'London'

    r = requests.get(url.format(city, api_key)).json()

    city_weather = {
        'city': r['name'],
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    context = {'city_weather': city_weather}
    return render(request, 'weather/weather.html', context)

