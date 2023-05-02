from django.contrib import admin
from django.contrib.admin import ModelAdmin 
from . models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','first_name', 'last_name', 'pix', 'email', 'address', 'phone', 'dob', 'nationality', 'gender', 'state']
admin.site.register(Profile, ProfileAdmin)