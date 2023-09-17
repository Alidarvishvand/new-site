from django import forms


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    mail = forms.EmailField(max_length=255)
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)