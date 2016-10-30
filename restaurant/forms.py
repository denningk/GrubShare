'''
Created on Oct 29, 2016

@author: denningk
'''
from django import forms
from django.core import validators

class DonationForm(forms.Form):
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description of Donation','class':'form-control','name':'description'}),max_length=200)
    approx_servings = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'How many people will this feed?','class':'form-control','name':'approx_servings'}),max_length=50)
