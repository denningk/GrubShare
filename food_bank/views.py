from django.shortcuts import render

def dashboard(request):
    return render(request, "food_bank_dashboard.html")
