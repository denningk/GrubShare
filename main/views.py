from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect

def landing_page(request):
    return render(request, "landing_page.html")

def restaurant_login_page(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        pass_word = request.POST.get('user_name')
        if Restaurant.objects.get(user_name = user_name).pass_word == pass_word:
            request.session['user_name'] = user_name
            return HttpResponseRedirect('/restaurant/donation')
        else:
            return HttpResponseRedirect('/')
