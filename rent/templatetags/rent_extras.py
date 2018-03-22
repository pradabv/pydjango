from django import template
import datetime
from ..models import Transaction

register = template.Library()

@register.filter
def is_room_occupied_test(room,lease):
    is_occupied = False
    for item in lease:
        if item.lease_room.room_id == room:
            is_occupied = True
            
    return is_occupied

@register.filter
def is_room_occupied(room,lease):
    is_occupied = False
    for item in lease:
        if item.lease_room.room_id == room and current_month_record(item):
            is_occupied = True
            
    return is_occupied

@register.filter
def get_matching_record(data_list,room):
    return data_list.filter(lease_room=room)

@register.filter
def get_lease_by_room(lease_details,room):
    for item in lease_details:
        if item.lease_room.room_id == room and current_month_record(item):
            return item     

@register.filter
def filter_current_lease(item):
    return  current_month_record(item)
            

@register.filter
def get_pending_month_count(lease_details,room):
    for item in lease_details:
        if item.lease_room.room_id == room and current_month_record(item):
            return item  

@register.filter
def getPendingAmountForRoom(lease_details,room_id):
    total_rent = 0
    for item in lease_details:
        if item.lease_room.room_id == room_id and not current_month_record(item):
            total_rent += item.lease_amount
    
    paid_amount = 0
    transaction = Transaction.objects.filter(transaction_room=room_id)
    for item in transaction:
        if item.transaction_reason == "Rent":
            paid_amount += item.transaction_amount
    
    balance = total_rent - paid_amount
    return balance
    
@register.filter
def getPendingAmountForTenant(tenant_id):
    return tenant_id  


@register.filter
def getPendingMonthCountForRoom(lease_details,room_id):
    current_room_count = 0
    for item in lease_details:
        if item.lease_room.room_id == room_id and not current_month_record(item):
            current_room_count += 1

    paid_amount_count = 0
    transaction = Transaction.objects.filter(transaction_room=room_id)
    for item in transaction:
        if item.transaction_reason == "Rent":
            paid_amount_count += 1
    
            
    return current_room_count - paid_amount_count
   
        


#helpers


def current_month_record(item):
    today = datetime.date.today()
    compare = item.lease_start_date <= today and today <= item.lease_end_date
    if compare: 
        return True
    else:
        return False