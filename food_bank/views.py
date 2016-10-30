from django.shortcuts import render
import googlemaps
import datetime
from main.models import *
from django.utils import timezone

gmaps = googlemaps.Client(key='AIzaSyAPdF9odAb32yaoEP-oR2fXdurUuBRsVVY')
coordList = []

def dashboard_map(request):

    donating_rests = Restaurant.objects.filter(restaurant_donation__date = datetime.date.today())

    for rest in donating_rests:
        data = gmaps.geocode(rest.street + ", " + rest.city + ", " + rest.state)
        print
        print data

    return render(request, "food_bank_dashboard.html")
