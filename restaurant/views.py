from django.shortcuts import render
from main.models import *
from django.http import HttpResponseRedirect
from datetime import datetime
from forms import *
from datetime import datetime

def restaurant_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)

        if form.is_valid():
            description = form.cleaned_data['donation_description']
            approx_servings = form.cleaned_data['approx_servings']
            date = datetime.date.today()
            restaurant_user_name = request.session['user_name']
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
