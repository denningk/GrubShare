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
    numRest = len(locations)
    restDict = []
    restNames = []
    currRest = Restaurant_Donation.objects.filter(date = datetime.date.today())
    
    i = 0
    j = 0
    
    for rest in currRest:
        
        restDict.append([rest.approx_servings, rest.description])
        
        i += 1
    
    for restName in donating_rests:
        restNames.append(restName.name)
        
    while j < i:
        restDict[j].append(restNames[j])
        j += 1
    
    return render(request, "map.html", {'locations':locations,'center':list(center),'numRest': numRest, 'restDict': restDict, 'restNames': restNames})

def dashboard(request):
    return render(request, "food_bank_dashboard.html")
