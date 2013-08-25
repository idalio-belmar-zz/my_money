# To change this template, choose Tools | Templates
# and open the template in the editor.
from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)