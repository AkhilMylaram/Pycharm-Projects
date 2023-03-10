from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(max_length=62533, widget=forms.Textarea)
    sender = forms.EmailField()