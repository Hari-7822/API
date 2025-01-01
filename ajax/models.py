from django.db import models
from django import forms

class Demo(models.Model):
    name= models.CharField(max_length=255)

class DemoForm(forms.Form):
    name= forms.CharField()
    class Meta:
        model=Demo
        fields=('__all__')