from django.contrib import admin

# Register your models here.

from .models import Location, Property, Room, Transaction, Leasedetails, Tenant

admin.site.register(Location)
admin.site.register(Property)
admin.site.register(Room)
admin.site.register(Transaction)
admin.site.register(Leasedetails)
admin.site.register(Tenant)