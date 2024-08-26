from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=4,
        widget=forms.TextInput(
            attrs = {"placeholder" : "username (4자리 이상)"}
        ))
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
            attrs = {"placeholder" : "password (4자리 이상)"}
        ))