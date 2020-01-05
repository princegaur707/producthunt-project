
from django.contrib import admin
from django.urls import path,include
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('accounts/',include('accounts.urls')),#directing towards the url folder of accounts
    path('products/',include('products.urls')),
]
