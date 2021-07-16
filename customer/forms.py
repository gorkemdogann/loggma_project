from django.db import models
from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
  tc : forms.Textarea(attrs={'rows': '3', 'minlength': 10,'maxlength': 11})

  class Meta:
    model=Customer
    fields = ["user","tc","name","surname","phone","city","district"]
