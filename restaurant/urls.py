'''
Created on Oct 29, 2016

@author: denningk
'''
from django.conf.urls import url
import restaurant.views as rev

urlpatterns = [

               url(r'^donation/', rev.restaurant_donation),
               url(r'^donation/submit', rev.restaurant_donation),
               url(r'^confirmation/', rev.confirmation),
               ]
