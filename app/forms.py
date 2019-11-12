from django import forms
from django.forms import ModelChoiceField
from app.models import Showing


class NewTicketForm(ModelChoiceField):
    def label_from_instance(self, showing):
        return "#%i" % showing.id
