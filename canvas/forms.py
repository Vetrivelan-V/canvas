#-*- coding: utf-8 -*-
from django import forms

from canvas.models import CanvasUser

from datetime import datetime

class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   def clean_message(self):
       username = self.cleaned_data.get("username")
       dbuser = CanvasUser.objects.filter(email_id=username)

       if not dbuser:
           raise forms.ValidationError("User does not exist in our db!")
       else:
           print(dbuser[0].ub_id)
           user=CanvasUser.objects.get(pk=dbuser[0].ub_id)
           user.last_login=datetime.now()
           user.save()
           return user