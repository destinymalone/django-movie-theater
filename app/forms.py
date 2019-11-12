from django import forms
from django.forms import ModelChoiceField
from app.models import Showing


class NewTicketForm(forms.Form):
    name = forms.CharField()
    showing_id = forms.IntegerField()
