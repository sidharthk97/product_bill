from django.contrib import admin
from django.urls import path

from . import views
app_name='bill'


urlpatterns=[
    path('', views.bill_index, name='bill_index'),
    path('billing', views.bill_billing, name='bill_billing'),

]



