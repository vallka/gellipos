from django.contrib import admin

from .models import *

# Register your models here.
#admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id_product','reference','name','ean13','quantity',]
    search_fields = ['id_product','reference','name','ean13', ]


class DetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 3

#admin.site.register(Order)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [DetailInline]
    list_display = ['id','customer_name','customer_email','total','status',]
    search_fields = ['id','customer_name','customer_email','total' ]
    list_filter = ['status']
