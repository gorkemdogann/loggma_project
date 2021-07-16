from django.contrib import admin
from django import forms
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

  list_display =  ['tc', 'name', 'surname', 'created_date']
  list_display_links = ['tc', 'name', 'surname']
  search_fields = ['tc', 'name', 'surname']
  list_filter = ['created_date']
  
  class Meta:
    model = Customer