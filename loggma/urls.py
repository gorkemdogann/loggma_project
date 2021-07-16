from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from customer import views    


urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('customer.urls')),
  path('', views.index, name='index'),
  path('user/', include('user.urls')),
]