from django.shortcuts import render,redirect
from .models import Subscriber
from .form import SubscriberForm

# Create your views here.

def subscriberView(request):
    pass



def subscriberForm(request):
    if request.method == 'POST':
        form=SubscriberForm(request.POST)

        if form.is_valid():
            post_email = form.data.get('email') 
            if Subscriber.objects.filter(email=post_email).exists():
                
    


