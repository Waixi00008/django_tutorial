from django import forms
from django.forms import fields

class Auth(forms.Form):
    username = fields.CharField(max_length=18,required=True)
    password = fields.CharField(widget=forms.PasswordInput)