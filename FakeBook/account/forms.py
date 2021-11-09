from django import forms

# Creating login form view
class LoginForm(forms.Form):
    username = forms.CharField()
    # Using PasswordInput widget to let browser know that is a password
    password = forms.CharField(widget=forms.PasswordInput)
