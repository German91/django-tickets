from django import forms

from .models import Ticket


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('title', 'description',)


class TicketEditForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('title', 'description', 'status',)
