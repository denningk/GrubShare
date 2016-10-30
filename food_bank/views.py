from django.shortcuts import render

def dashboard(request):
    return render(request, "food_bank_dashboard.html")

def map(request):
    return render(request,"map.html", {"center":[-79.4414, 37.7858]})