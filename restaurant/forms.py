'''
Created on Oct 29, 2016

@author: denningk
'''
from django import forms
from django.core import validators

class DonationForm(forms.Form):
    
    donation_description = forms.CharField(widget=forms.Textarea(attrs={'name':'donation_description'}))
    approx_servings = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Approx Servings','class':'form-control','name':'approx_servings'}),max_length=50)
