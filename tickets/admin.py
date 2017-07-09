from django.contrib import admin

from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Ticket, TicketAdmin)
