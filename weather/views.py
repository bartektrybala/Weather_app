import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    api_key = '69238c44a6a9aee21feb1688f347b607'
    
    err_msg = ''

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            
            if existing_city_count == 0:
                form.save()
            else:
                err_msg = 'City already exists in the database!'

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:


        r = requests.get(url.format(city, api_key)).json()

        city_weather = {
            'city': r['name'],
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)


    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)

