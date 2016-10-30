from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect

def landing_page(request):
    return render(request, "landing_page.html")

def restaurant_login_page(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        pass_word = request.POST.get('pass_word')
        try:
            Restaurant.objects.get(user_name = username, pass_word = pass_word)
            request.session['user_name'] = username
            return HttpResponseRedirect('/restaurant/donation')
        except:
            return render(request, "landing_page.html", {'rest_error_msg': "Wrong username or password. Please try again."})

def food_bank_login_page(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        pass_word = request.POST.get('pass_word')
        try:
            Food_Bank.objects.get(user_name = username, pass_word = pass_word)
            request.session['user_name'] = username
            return HttpResponseRedirect('/food_bank/dashboard')
        except:
            return render(request, "landing_page.html", {'food_error_msg': "Wrong username or password. Please try again."})
