from django.shortcuts import render

# Create your views here.

def restaurant_form(request):
    return render("restaurant_form.html")

def foodBank_form(request):
    return render("foodbank_form.html")

def register_restaurant(request):
    pass

def register_foodbank(request):
    pass