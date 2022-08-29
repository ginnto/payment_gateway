from django.shortcuts import render
from django.conf import settings
from . models import *
import razorpay
# Create your views here.
def home(request):

    return render(request,'index.html')


client = razorpay.Client(auth = (settings.RAZORPAY_API_KEY,settings.RAZORPAY_API_SECRET_KEY))

def donate(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        email = request.POST.get('email')

        info = donate(name=name, email=email, amount=amount)
        info.save()


    DATA = {
        "amount": 100,
        "currency": "INR",
        }
    payment_order = client.order.create(data=DATA)
    payment_order_id = payment_order['id']
    context = {
        'order_id' : payment_order_id
    }


    return render(request,'details.html',context)