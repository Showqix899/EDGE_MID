from django import forms

from .models import Subscriber


class SubscriberForm(forms.Form):

    class Meta:
        model=Subscriber
        fields=['name','email']