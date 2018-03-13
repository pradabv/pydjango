from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('property', views.property, name='property'),
    path('property_details/<int:property_id>', views.property_details, name='property_details'),
    path('room_details/<int:room_id>', views.room_details, name='room_details'),
    path('transactions', views.transaction_list, name='transactions'),
    path('tenants', views.tenants_list, name='tenants'),
    path('lease', views.lease_list, name='lease'),
    path('tenant_details/<int:tenant_id>', views.transaction_list, name='tenant_details'),
]