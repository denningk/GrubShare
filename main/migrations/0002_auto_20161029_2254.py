# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant_donation',
            name='food_bank_pickup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Food_Bank_Pickup'),
        ),
    ]