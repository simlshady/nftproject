from django import forms


class SendEmailForm(forms.Form):
    first_name = forms.CharField(max_length=350)
    last_name = forms.CharField(max_length=350)
    email = forms.EmailField()
    message = forms.TextInput()