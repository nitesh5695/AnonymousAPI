

from django.contrib import admin
from .models import anonymousUser,customer_model
class anonymousadmin(admin.ModelAdmin):
    list_display=['id','username']
admin.site.register(anonymousUser,anonymousadmin)


@admin.register(customer_model)
class CustomerAdmin(admin.ModelAdmin):
 list_display = ['id', 'mobile', 'customer_type']    

# Register your models here.
