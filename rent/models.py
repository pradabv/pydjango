from django.db import models

# Create your models here.

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now=True) 

class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    property_name = models.CharField(max_length=300)
    property_location = models.ForeignKey(Location, on_delete=models.CASCADE) 
    timestamp = models.DateTimeField(auto_now=True) 

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_property = models.ForeignKey(Property, on_delete=models.CASCADE) 
    room_name = models.CharField(max_length=50)
    room_rent = models.DecimalField(max_digits=8,decimal_places=2)
    room_description = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now=True)

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(max_digits=8,decimal_places=2)
    transaction_date = models.DateField()
    transaction_reason = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now=True) 

class Tenant(models.Model):
    tenant_id =  models.AutoField(primary_key=True)
    tenant_name =  models.CharField(max_length=250)
    tenant_company =  models.CharField(max_length=250)
    tenant_description = models.CharField(max_length=500)
    tenant_joindate = models.DateField()
    tenant_contact = models.IntegerField(unique=True)
    tenant_secondry = models.IntegerField(unique=True)
    timestamp = models.DateTimeField(auto_now=True)

class Leasedetails(models.Model):
    lease_id = models.AutoField(primary_key=True)
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()
    lease_amount = models.DecimalField(max_digits=8,decimal_places=2)
    lease_tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    lease_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    lease_transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lease_room.room_name +" - "+ str(self.lease_start_date)



    
