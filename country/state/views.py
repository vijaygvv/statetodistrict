from django.shortcuts import render
from .models import State, City

def city_list(request):
    states = State.objects.all()
    print(states)
    cities = City.objects.all()
    print(cities)
    return render(request, 'city_list.html', {'states': states, 'cities': cities})
