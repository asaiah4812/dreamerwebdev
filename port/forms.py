from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message',)