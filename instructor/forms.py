from django import forms
from .models import Instructor



class InstructorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = Instructor
        fields = ('emailid', 'password')


