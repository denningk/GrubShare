'''
Created on Oct 29, 2016

@author: denningk
'''
from django.conf.urls import url
import food_bank.views as fbv

urlpatterns = [
               url(r'^dashboard/', fbv.dashboard),
               ]
