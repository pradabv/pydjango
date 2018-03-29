from django.shortcuts import render, loader
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from .models import Location, Property, Room, Transaction, Leasedetails, Tenant
from django.db.models import Count, Avg, Sum, Min, Q
from django.core import serializers
import json
from datetime import datetime

# Create your views here.

def index(request):
    latest_question_list = Location.objects.order_by('-location_name')[:5]
    template = loader.get_template('rent/property.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    return HttpResponse("create")

def property(request):
    location = Location.objects.all();
    room = Room.objects.all();
    property = Property.objects.all();
    #property_details = Property.objects.values('property_id','property_name','property_location_id' ).annotate(num_room=Count('room')).order_by('property_id')
    property_details = Property.objects.all().annotate(num_room=Count('room')).order_by('property_id')
    string_data = []#serializers.serialize('json', property_details)
    #room_count = Room.objects.all().values('room_property').annotate(num_room=Count('room_property')).order_by('room_property')
    print(property_details)
    return render(request,'rent/property_list.html',{'location':location,'room':room,'property':property, 'room_count':property_details, 'string_data':string_data})

def property_details(request, property_id):
    room = Room.objects.filter(room_property_id=property_id)
    lease_details = Leasedetails.objects.filter(lease_room__in=room)
    string_data = serializers.serialize('json',lease_details)
    return render(request,'rent/property_details.html',{'room':room,'lease_details':lease_details,'string_data':string_data})

def transaction_list(request):
    transaction = Transaction.objects.all()
    return render(request,'rent/transaction.html',{'transaction_list':transaction})

def room_details(request, room_id):
    room = Room.objects.get(room_id=room_id)
    lease_details = Leasedetails.objects.filter(lease_room=room_id)
    if not lease_details:
        lease_details = []
    return render(request,'rent/room_details.html',{'room_details':room,'lease_details':lease_details})

def tenants_list(request):
    tenant = Tenant.objects.all()
    return render(request,'rent/tenant_list.html',{'tenant_list':tenant})

def tenant_details(request, tenant_id):
    tenant = Tenant.objects.get(tenant_id=tenant_id)
    lease = Leasedetails.objects.filter(lease_tenant=tenant_id).order_by('lease_room__room_name','lease_start_date')
    lease_start_date = Min('leasedetails__lease_start_date')   
    total_rent = Sum('leasedetails__lease_amount')
    pending_months = Count('leasedetails__lease_amount',filter=Q(leasedetails__lease_transaction__isnull=True))
    balance_amount =  total_rent - Sum('leasedetails__lease_transaction__transaction_amount')
  
    tenant_rooms = Room.objects.filter(leasedetails__lease_tenant=tenant_id)
    room_wise_lease = tenant_rooms.annotate(start_date=lease_start_date,total_rent=total_rent,balance_amount=balance_amount,pending_months=pending_months).order_by('room_name')
    return render(request,'rent/tenant_details.html',{'tenant_details':tenant,'lease_details':lease,'lease_room_wise':room_wise_lease})

def lease_list(request):
    lease = Leasedetails.objects.all()
    return render(request,'rent/lease_list.html',{'lease_list':lease})

def lease_details(request):
    lease = Leasedetails.objects.all()
    return render(request,'rent/room_details.html',{'lease_details':lease})

def lease_create(request,room_id):
    
    
    
    if request.method == "POST":
        room_id =  request.POST.get('room_id')
        start_Date =  request.POST.get('start_date')
        end_Date =  request.POST.get('end_date')
        lease_amount =  request.POST.get('lease_amount')
        tenant_id =  request.POST.get('tenant_id')
        
        valid_start_Date = datetime.strptime(start_Date, '%Y-%m-%d')
        valid_end_Date = datetime.strptime(end_Date, '%Y-%m-%d')
        
        
        lease = Leasedetails(lease_start_date= valid_start_Date,
        lease_end_date= valid_end_Date,
        lease_amount= lease_amount,
        lease_tenant= Tenant(tenant_id=tenant_id),
        lease_room= Room(room_id=room_id))

        lease.save()
        room = Room.objects.get(room_id=room_id)
        return HttpResponseRedirect('/rent/property/property_details/%i'% room.room_property.property_id)


    room = Room.objects.get(room_id=room_id)
    tenant_list = Tenant.objects.all()
    last_lease = Leasedetails.objects.filter(lease_room=room).order_by('-lease_end_date')[:1]
    if last_lease:
        last_lease = last_lease[0]
    #print(last_lease.lease_tenant.tenant_id)
    return render(request,'rent/lease_create.html',{'room':room,'tenant_list':tenant_list,'last_lease':last_lease})

def transactions_create(request, lease_id):
    if request.method == "POST":
        room_id =  request.POST.get('room_id')
        start_Date =  request.POST.get('start_date')
        end_Date =  request.POST.get('end_date')
        lease_amount =  request.POST.get('lease_amount')
        tenant_id =  request.POST.get('tenant_id')
        
        valid_start_Date = datetime.strptime(start_Date, '%Y-%m-%d')
        valid_end_Date = datetime.strptime(end_Date, '%Y-%m-%d')
        
        
        lease = Leasedetails(lease_start_date= valid_start_Date,
        lease_end_date= valid_end_Date,
        lease_amount= lease_amount,
        lease_tenant= Tenant(tenant_id=tenant_id),
        lease_room= Room(room_id=room_id))

        lease.save()
        room = Room.objects.get(room_id=room_id)
        return HttpResponseRedirect('/rent/property/property_details/%i'% room.room_property.property_id)


    lease = Leasedetails.objects.get(lease_id=lease_id)
    tenant_list = Tenant.objects.all()
    return render(request,'rent/transactions_create.html',{'lease':lease,'tenant_list':tenant_list})

    

def get_country_list(request):
    tenant = Tenant.objects.values('tenant_id','tenant_name')
    #return render(request,'rent/lease_create.html',{'lease_details':lease})
    #string_data = json.dump(lease,fp)
    #return JsonResponse(list(lease),safe=False)
    x =[
      {'id': "someId1", 'name': "Display name 1"},
      {'id': "someId2", 'name': "Display name 2"}
    ]
    return JsonResponse(list(tenant),safe=False)

