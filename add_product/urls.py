from django.contrib import admin
from django.urls import path

from . import views
app_name='add_product'



urlpatterns=[
    
    path('add', views.add_product_add, name='add_product_add'),

]



