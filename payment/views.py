from django.shortcuts import render

# Create your views here.
def checkout(request):
    return render(request, 'checkout.html')

def order_success(request):
    return render(request , 'order-success.html')