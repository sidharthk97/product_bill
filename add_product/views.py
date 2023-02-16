from django.shortcuts import render

# Create your views here.

def add_product_add(request):
    return render(request, 'add_product_templates/add.html')