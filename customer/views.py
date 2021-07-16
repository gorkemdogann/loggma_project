from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q



@login_required(login_url = "user:login")
def index(request):
  customers = Customer.objects.filter(user=request.user)

  query = request.GET.get('q')

  if query:
    customers = customers.filter(
      Q(tc__icontains=query) |
      Q(name__icontains=query) |
      Q(surname__icontains=query) |
      Q(city__icontains=query)
    ).distinct()

  paginator = Paginator(customers, 25)
  page = request.GET.get('page')
  try:
    customers = paginator.page(page)
  except PageNotAnInteger:
    customers = paginator.page(1)
  except EmptyPage:
    customers = paginator.page(paginator.num_pages)

  return render(request, 'index.html', {'customers': customers})


def detail(request, id):
  customer = get_object_or_404(Customer, id=id)
  return render(request, 'detail.html',{"customer":customer})


@login_required(login_url = "user:login")
def addcustomer(request):
  form = CustomerForm(request.POST or None)

  if form.is_valid():
    customer = form.save(commit=False)

    customer.user = request.user
    customer.save()
    messages.success(request,"Müşteri kayıtı başarıyla oluşturuldu.")
    return redirect('customer:index')

  return render(request,'addcustomer.html',{"form":form})


@login_required(login_url = "user:login")
def UpdateCustomer(request, id):
  customer = get_object_or_404(Customer, id = id)
  form = CustomerForm(request.POST or None, request.FILES or None,instance=customer)
  if form.is_valid():
    customer = form.save(commit=False)
    customer.user = request.user
    customer.save()
    messages.success(request,"Müşteri bilgisi başarıyla güncellendi.")
    return redirect('customer:index')

  return render(request, 'update.html', {"form":form})


@login_required(login_url = "user:login")
def DeleteCustomer(request, id):
  customer = get_object_or_404(Customer, id = id)
  customer.delete()
  messages.warning(request,'Müşteri başarıyla silindi.')
  return redirect('customer:index')
