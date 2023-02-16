from django.shortcuts import render

# Create your views here.


def bill_billing(request):
    return render(request, 'bill_templates/billing.html')

def bill_index(request):
    return render(request, 'bill_templates/index.html')