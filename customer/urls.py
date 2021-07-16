from django.contrib import admin
from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
  path('', views.index, name='index'),
  path('addcustomer/',views.addcustomer, name='addcustomer'),
  path('detail/<int:id>',views.detail, name='detail'),
  path('update/<int:id>',views.UpdateCustomer, name='updatecustomer'),
  path('delete/<int:id>',views.DeleteCustomer, name='deletecustomer'),
]