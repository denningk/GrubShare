from django.contrib import admin
from main.models import *
# Register your models here.
"""
class Admin(admin.ModelAdmin):  
    list_display = ('title' , 'location','post_time', 'valid_till')
    list_filter = ['post_time','valid_till']
    ordering = ('-post_time',)"""

admin.site.register(Restaurant)
admin.site.register(Food_Bank)
admin.site.register(Area)
admin.site.register(Restaurant_Donation)
admin.site.register(Food_Bank_Pickup)