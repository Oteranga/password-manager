from django import forms

class RegisterForm(forms.Form):
   username = forms.CharField()
   email = forms.CharField()
   password = forms.CharField()
   masterpassword = forms.CharField()
