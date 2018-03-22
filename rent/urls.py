from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('property', views.property, name='property'),
    path('property/property_details/<int:property_id>', views.property_details, name='property_details'),
    path('room_details/<int:room_id>', views.room_details, name='room_details'),
    path('transactions', views.transaction_list, name='transactions'),
    path('tenants', views.tenants_list, name='tenants'),
    path('lease', views.lease_list, name='lease'),
    path('lease/create/<int:room_id>', views.lease_create, name='lease_create'),
    path('tenants/tenant_details/<int:tenant_id>', views.tenant_details, name='tenant_details'),
    path('ajax/get_country_list', views.get_country_list, name='get_country_list'),
]