import django_filters

from .models import Ticket


class TicketStatusFilter(django_filters.FilterSet):

    class Meta:
        model = Ticket
        fields = ('status',)
