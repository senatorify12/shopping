from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . models import *

# Register your models here.
# py manage.py createsuperuser
# admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'slug', 'img','description']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category','title','slug', 'price','img','brands','description',
     'max_quantity', 'min_quantity', 'date_uploaded','date_updated']
admin.site.register(Product, ProductAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','firstName', 'lastName', 'subject','email', 'message',
     'date_created','status']
admin.site.register(Contact, ContactAdmin)

class ShopcartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'title', 'quantity', 
    'order_no', 'amount', 'paid', 'price', 'date_created']
admin.site.register(Shopcart, ShopcartAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 
    'email', 'amount', 'paid', 'phone', 'shop_code', 'pay_code', 'pay_date']
admin.site.register(Payment, PaymentAdmin)
