'''
Created on Oct 29, 2016

@author: aminm
'''
from django.conf.urls import url
import registration.views as rv

urlpatterns = [
               
               url(r'^restaurant/', rv.register_restaurant),
               url(r'^foodbank/', rv.foodBank_form),
               url(r'^restaurant/register', rv.register_restaurant),
               url(r'^foodbank/register', rv.register_foodbank),             
               ]