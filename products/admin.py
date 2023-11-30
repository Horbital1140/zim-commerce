from django.contrib import admin
from .models import product_details, funding, offer, department

class product_detailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name', 'price', 'stock')

class fundingAdmin(admin.ModelAdmin):
    list_display = ('email', 'amount')
    search_fields = ('email', 'amount')

class offerAdmin(admin.ModelAdmin):
    list_display = ['code', 'description', 'discount']
    search_fields = ['code', 'description', 'discount']


class departmentAdmin(admin.ModelAdmin):
    list_display = ['unit', 'grade']
    search_fields = ['unit', 'grade']


admin.site.register(product_details, product_detailsAdmin)
admin.site.register(funding, fundingAdmin)
admin.site.register(offer, offerAdmin)
admin.site.register(department, departmentAdmin)
