#-*- coding: utf-8 -*-
from django import forms

from canvas.models import CanvasUser

from datetime import datetime

class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   def clean_message(self):
       username = self.cleaned_data.get("username")
       password=self.cleaned_data.get("password")
       dbuser = CanvasUser.objects.filter(email_id=username)

       if not dbuser:
           raise forms.ValidationError("User does not exist in our db!")
       else:
           if dbuser[0].password == password:
               print(dbuser[0].ub_id)
               dbuser[0].last_login=datetime.now()
               dbuser[0].save()
               return dbuser[0]
           else:
               raise forms.ValidationError("User password does not match")

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )