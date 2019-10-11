from django.contrib import admin
from .models import Image,Location,Category
# Register your models here.

# class LocationAdmin(admin.ModelAdmin):
#     filter_horizontal =('location_name',)
    
# class CategoryAdmin(admin.ModelAdmin):
#     filter_horizontal =('img_category',)    
    
    
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)