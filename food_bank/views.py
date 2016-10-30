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
    return float(longi), float(lati)
def dashboard_map(request):

    donating_rests = Restaurant.objects.filter(restaurant_donation__date = datetime.date.today())
    locations = []
    current_food_bank = Food_Bank.objects.get(user_name = request.session['user_name'])
    fb_location = gmaps.geocode(current_food_bank.street+ ", " + current_food_bank.city + ", " + current_food_bank.state)
    center = parse_location(fb_location)
    for rest in donating_rests:
        data = gmaps.geocode(rest.street + ", " + rest.city + ", " + rest.state)        
        locations.append(list(parse_location(data)))
    return render(request, "map.html", {'locations':locations,'center':list(center)})


def map(request):
    return render(request,"map.html", {"center":[-79.4414, 37.7858]})
