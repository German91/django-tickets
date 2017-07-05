from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Ticket


@login_required()
def ticket_list(request):
    tickets = Ticket.objects.filter(status='open', creator=request.user)
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})
