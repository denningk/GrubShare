'''
Created on Oct 29, 2016

@author: aminm
'''
from django import forms
from django.core import validators

class RestaurantRegistrationForm(forms.Form):
    
    name = forms.CharField(label="Name",widget=forms.TextInput(attrs={'placeholder': 'Name','class':'form-control', 'name':'name'}),max_length=200)
    address_street=  forms.CharField(label="Street",widget=forms.TextInput(attrs={'placeholder': 'Street','class':'form-control','name':'address_street' }),max_length=200)
    address_city = forms.CharField(label="City",widget=forms.TextInput(attrs={'placeholder': 'City','class':'form-control', 'name':'address_city'}),max_length=200)
    address_state = forms.CharField(label="State",widget=forms.TextInput(attrs={'placeholder': 'State','class':'form-control', 'name':'address_state'}),max_length=20)
    address_zip = forms.CharField(label="Zip",widget=forms.TextInput(attrs={'placeholder': 'Zip','class':'form-control', 'name':'address_zip'}),max_length=12)

    email = forms.EmailField(label="E-mail",widget=forms.EmailInput(attrs={'placeholder': 'E-mail','class':'form-control', 'email':'email'}))
    contact_first_name = forms.CharField(label="Contact Person's First Name",widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'form-control', 'name':'contact_first_name'}),max_length=100)
    contact_last_name = forms.CharField(label="Contact Person's Last Name",widget=forms.TextInput(attrs={'placeholder': 'Last Name','class':'form-control','name':'contact_last_name' }),max_length=200)
    contact_number = forms.CharField(label="Phone Number",widget=forms.TextInput(attrs={'placeholder': 'Phone Number','class':'form-control', 'name':'contact_number'}),max_length=50)
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control', 'name':'username'}),max_length=30,min_length=3,validators=[validators.validate_slug])
    password = forms.CharField(label="Password",max_length=50,min_length=6,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password','class':'form-control', 'name':'password'}))
   
    
    
class FoodBankForm(forms.Form):
       
    name = forms.CharField(label="Name",widget=forms.TextInput(attrs={'placeholder': 'Name','class':'form-control', 'name':'name'}),max_length=200)
    address_street=  forms.CharField(label="Street",widget=forms.TextInput(attrs={'placeholder': 'Street','class':'form-control','name':'address_street' }),max_length=200)
    address_city = forms.CharField(label="City",widget=forms.TextInput(attrs={'placeholder': 'City','class':'form-control', 'name':'address_city'}),max_length=200)
    address_state = forms.CharField(label="State",widget=forms.TextInput(attrs={'placeholder': 'State','class':'form-control', 'name':'address_state'}),max_length=20)
    address_zip = forms.CharField(label="Zip",widget=forms.TextInput(attrs={'placeholder': 'Zip','class':'form-control', 'name':'address_zip'}),max_length=12)

    email = forms.EmailField(label="E-mail",widget=forms.EmailInput(attrs={'placeholder': 'E-mail','class':'form-control', 'email':'email'}))
    contact_first_name = forms.CharField(label="Contact Person's First Name",widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'form-control', 'name':'contact_first_name'}),max_length=100)
    contact_last_name = forms.CharField(label="Contact Person's Last Name",widget=forms.TextInput(attrs={'placeholder': 'Last Name','class':'form-control','name':'contact_last_name' }),max_length=200)
    contact_number = forms.CharField(label="Phone Number",widget=forms.TextInput(attrs={'placeholder': 'Phone Number','class':'form-control', 'name':'contact_number'}),max_length=50)
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control', 'name':'username'}),max_length=30,min_length=3,validators=[validators.validate_slug])
    password = forms.CharField(label="Password",max_length=50,min_length=6,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password','class':'form-control', 'name':'password'}))    