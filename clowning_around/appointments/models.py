from django.db import models
from django.db.models import PROTECT
from django.utils.translation import ugettext_lazy as _
from clowning_around.users.models import Client, Troupe

appointment_statuses = (
    ('1', 'upcoming'),
    ('2', 'incipient'),
    ('3', 'completed'),
    ('4', 'cancelled')
)


class Appointment(models.Model):
    date = models.DateField(_("Date"), auto_now_add=True, blank=True)
    time = models.TimeField(_("Time"), auto_now_add=True, blank=True)
    address = models.CharField(_("Address"), max_length=128)
    venue = models.CharField(_("Venue"), max_length=30)
    status = models.CharField(_("Status"), choices=appointment_statuses, default=1, max_length=15)
    created_by = models.CharField(max_length=30)  # TroupeLeader name
    # Troupe leader assigns appointment to troupe
    troupe = models.ForeignKey(Troupe, on_delete=models.CASCADE)  # A troupe may have many appointments
    clients = models.ManyToManyField(Client)


# Clients to: Rate a past appointment with clown face emojis
class Rating(models.Model):
    """
    An emoji name can be posted from Postman while testing this.
    If UI is present, a list of all emojis (by the image) can be displayed for choice

    The image links of all the emojis can be retrieved using EmojiJSONListView.as_view()
    """
    emoji_name = models.CharField(max_length=50)
    appointment = models.ForeignKey(Appointment, on_delete=PROTECT)


# clowns to: Report an issue with an appointment (not a state change)
class Issue(models.Model):
    text = models.TextField(max_length=500)
    appointment = models.ForeignKey(Appointment, on_delete=PROTECT)


# Request client contact details, with a reason for the request
class ClientContactRequest(models.Model):
    reason = models.TextField(max_length=500)
    client_name = models.CharField(max_length=50)
    # TODO: Later, include the name of the clown that makes the request
