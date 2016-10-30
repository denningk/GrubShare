from django.shortcuts import render
from main.models import *
from django.http import HttpResponseRedirect
from datetime import datetime
from .forms import *
from datetime import datetime

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
    return render(request, 'foodbank_form.html', {'form': form})
