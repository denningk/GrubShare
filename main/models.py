from __future__ import unicode_literals
from django.db import models

class Area(models.Model):
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)

    def __str__(self):
        return self.city

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    first_name_contact = models.CharField(max_length=200)
    last_name_contact = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    pass_word = models.CharField(max_length=200)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Food_Bank(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    first_name_contact = models.CharField(max_length=200)
    last_name_contact = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    pass_word = models.CharField(max_length=200)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Food_Bank_Pickup(models.Model):
    date = models.DateTimeField('donation date')
    food_bank = models.ForeignKey(Food_Bank, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)

class Restaurant_Donation(models.Model):
    description = models.CharField(max_length=200)
    approx_servings = models.IntegerField(default=0)
    date = models.DateTimeField('donation date')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_bank_pickup = models.ForeignKey(Food_Bank_Pickup, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.restaurant.name
