'''
Created on Oct 29, 2016

@author: aminm
'''
from django import forms
from django.core import validators


class RestaurantRegistrationForm(forms.Form):
    
    name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Name','class':'form-control'}),max_length=200)
    address_street=  forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Street','class':'form-control'}),max_length=200)
    address_city = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'City','class':'form-control'}),max_length=200)
    address_state = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'State','class':'form-control'}),max_length=20)
    address_zip = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Zip','class':'form-control'}),max_length=12)

    email = forms.EmailField()
    contact_first_name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'form-control'}),max_length=100)
    contact_last_name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Last Name','class':'form-control'}),max_length=200)
    contact_number = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Phone Number','class':'form-control'}),max_length=50)
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}),max_length=30,min_length=3,validators=[validators.validate_slug])
    password = forms.CharField(label="",max_length=50,min_length=6,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password','class':'form-control', 'id':'password1'}))
   
    
    
class FoodBank(forms.Form):
    name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Name','class':'form-control'}),max_length=200)
    address_street=  forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Street','class':'form-control'}),max_length=200)
    address_city = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'City','class':'form-control'}),max_length=200)
    address_state = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'State','class':'form-control'}),max_length=20)
    address_zip = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Zip','class':'form-control'}),max_length=12)
    email = forms.EmailField()
    contact_first_name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'form-control'}),max_length=100)
    contact_last_name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Last Name','class':'form-control'}),max_length=200)
    contact_number = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Phone Number','class':'form-control'}),max_length=50)
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}),max_length=30,min_length=3,validators=[validators.validate_slug])
    password = forms.CharField(label="",max_length=50,min_length=6,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password','class':'form-control', 'id':'password1'}))
    
    
    
class DonationForm(forms.Form):
    donation_description = forms.CharField(widget=forms.Textarea)
    approx_servings = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Approx Servings','class':'form-control'}),max_length=50)
    date = forms.DateField(label=u'Date of Donation', input_formats=['%d/%m/%Y', '%m/%d/%Y',], required=False, widget=forms.DateInput(format = '%d/%m/%Y'))
    