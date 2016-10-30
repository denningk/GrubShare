from django.shortcuts import render
import googlemaps
import datetime
from main.models import *
from django.utils import timezone

gmaps = googlemaps.Client(key='AIzaSyAPdF9odAb32yaoEP-oR2fXdurUuBRsVVY')
coordList = []
def parse_location(json):
    data = json[0]
    lati = data['geometry']['location']['lat']
    longi =  data['geometry']['location']['lng']
    return float(lati), float(longi)
def dashboard_map(request):

    donating_rests = Restaurant.objects.filter(restaurant_donation__date = datetime.date.today())
    locations = []
    for rest in donating_rests:
        data = gmaps.geocode(rest.street + ", " + rest.city + ", " + rest.state)
        
        locations.append(list(parse_location(data)))

    return render(request, "food_bank_dashboard.html", {'locations':locations})

def dashboard(request):
    return render(request, "food_bank_dashboard.html")

def map(request):
    return render(request,"map.html", {"center":[-79.4414, 37.7858]})
