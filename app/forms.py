from django.db import forms
from app.models import Showing


class NewTicketForm(forms.Form):
    name = forms.TextField()
    showing_id = forms.ForeignKey(Showing, on_delete=forms.PROTECT)
