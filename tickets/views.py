from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Ticket
from .forms import TicketForm, TicketEditForm
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
            messages.add_message(request, messages.SUCCESS, 'Ticket successfuly created')
            return redirect('ticket_list')
    return render(request, 'tickets/ticket_create.html', {'form': form})


@login_required
def ticket_edit(request, slug):
    ticket = get_object_or_404(Ticket, slug=slug, creator=request.user)
    form = TicketEditForm(instance=ticket)
    if request.method == 'POST':
        form = TicketEditForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save(commit=True)
            messages.add_message(request, messages.SUCCESS, 'Ticket successfuly updated')
    return render(request, 'tickets/ticket_edit.html', {'form': form, 'ticket': ticket})


@login_required
def ticket_delete(request):
    pk = int(request.POST['pk'])
    ticket = get_object_or_404(Ticket, pk=pk, creator=request.user)
    ticket.delete()
    return HttpResponse('Ticket successfuly removed')
