# forms.py for pictorial project

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField()

