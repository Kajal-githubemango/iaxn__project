from django.contrib import admin
from .models import contact, servicesmodel, pricemodel



class Adminpricemodel(admin.ModelAdmin):
    list_display= ['price', 'offer']

class Adminservice(admin.ModelAdmin):
    list_display= ['title', 'desc']
    
class Admincontact(admin.ModelAdmin):
    list_display= ['name', 'address', 'city', 'state']
    
    
admin.site.register(contact, Admincontact)
admin.site.register(servicesmodel, Adminservice)
admin.site.register(pricemodel, Adminpricemodel)

# Register your models here.
