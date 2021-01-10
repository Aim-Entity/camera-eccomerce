from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'c-name', "placeholder": "Full Name"}), label='')

    email = forms.CharField(widget=forms.EmailInput(
        attrs={'id': 'c-email', "placeholder": "Email Address"}), label='')

    message = forms.CharField(widget=forms.Textarea(
        attrs={'id': 'c-msg', "placeholder": "Your Message"}), label='')

    # LABEL IS NEEDED TO COMPLY WITH CRISPY FORMS
    class Meta:
        model = Contact
        fields = ("fullname", "email", "message")
