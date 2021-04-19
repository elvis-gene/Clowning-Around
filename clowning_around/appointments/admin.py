from django.contrib import admin
from clowning_around.appointments.models import Appointment, Issue, Rating, ClientContactRequest

admin.site.register(Appointment)
admin.site.register(Rating)
admin.site.register(Issue)
admin.site.register(ClientContactRequest)
