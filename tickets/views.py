from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Ticket
from .forms import TicketForm
from .filters import TicketStatusFilter


@login_required()
def ticket_list(request):
    tickets = Ticket.objects.filter(creator=request.user)
    ticket_filter = TicketStatusFilter(request.GET, queryset=tickets)
    return render(request, 'tickets/ticket_list.html', {'tickets': ticket_filter})


@login_required
def ticket_create(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.creator = request.user
            ticket.save()

            return redirect('ticket_list')
    return render(request, 'tickets/ticket_create.html', {'form': form})
