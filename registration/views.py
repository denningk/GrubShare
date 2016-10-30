from django.shortcuts import render
from main.models import *
from django.http import HttpResponseRedirect
from datetime import datetime
from .forms import *
from datetime import datetime
def restaurant_form(request):
    return render(request, 'restaurant_registration_form.html')

def foodBank_form(request):
    return render(request,"foodbank_registration_form.html")

def register_restaurant(request):
    if request.method == 'POST':
        form = RestaurantRegistrationForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            street = form.cleaned_data['address_street']
            city = form.cleaned_data['address_city']
            zipcode = form.cleaned_data['address_zip']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['contact_number']
            first_name_contact = form.cleaned_data['contact_first_name']
            last_name_contact = form.cleaned_data['contact_last_name']
            user_name = form.cleaned_data['username']
            pass_word = form.cleaned_data['password']
            if not Area.objects.all().filter(zipcode = zipcode).exists():
                area = Area(city = city, zipcode = zipcode)
                area.save()
            restaurant_registration = Restaurant(name = name,
                                                street = street,
                                                city = city,
                                                zipcode = zipcode,
                                                email = email,
                                                phone_number = phone_number,
                                                first_name_contact = first_name_contact,
                                                last_name_contact = last_name_contact,
                                                user_name = user_name,
                                                pass_word = pass_word,
                                                area = Area.objects.get(zipcode = zipcode))
            restaurant_registration.save()
            return HttpResponseRedirect('/')
    else:
        form = RestaurantRegistrationForm()
    return render(request, 'restaurant_registration_form.html', {'form': form})


def register_foodbank(request):
    if request.method == 'POST':
        form = FoodBankForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            street = form.cleaned_data['address_street']
            city = form.cleaned_data['address_city']
            zipcode = form.cleaned_data['address_zip']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['contact_number']
            first_name_contact = form.cleaned_data['contact_first_name']
            last_name_contact = form.cleaned_data['contact_last_name']
            user_name = form.cleaned_data['username']
            pass_word = form.cleaned_data['password']
            if not Area.objects.all().filter(zipcode = zipcode).exists():
                area = Area(city = city, zipcode = zipcode)
                area.save()
            food_bank_registration = Food_Bank(name = name,
                                                street = street,
                                                city = city,
                                                zipcode = zipcode,
                                                email = email,
                                                phone_number = phone_number,
                                                first_name_contact = first_name_contact,
                                                last_name_contact = last_name_contact,
                                                user_name = user_name,
                                                pass_word = pass_word,
                                                area = area)
            food_bank_registration.save()
            return HttpResponseRedirect('/')
    else:
        form = FoodBankForm()
    return render(request, 'foodbank_registration_form.html', {'form': form})

def restuarant_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)

        if form.is_valid():
            description = form.cleaned_data['donation_description']
            approx_servings = form.cleaned_data['approx_servings']
            date = datetime.now()
            restaurant_user_name = form.cleaned_data['username']
            restaurant = Restaurant.objects.get(user_name=restaurant_user_name)

            donation = Restaurant_Donation(description = description,
                                            approx_servings = approx_servings,
                                            date = date,
                                            restaurant = restaurant)
            donation.save()
            return HttpResponseRedirect('/')
    else:
        form = DonationForm()
    return render(request, 'donation_form.html', {'form': form})
