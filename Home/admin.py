from django.contrib import admin
from Home.models import Customer,Product,std,Category

# Register your models here.


class data1(admin.ModelAdmin):
     list_display = ['name','email','address','password']

class productdisplay(admin.ModelAdmin):
     list_display = ['pname','price','description','image']

  
admin.site.register(Customer,data1)
admin.site.register(Category)
admin.site.register(Product,productdisplay)