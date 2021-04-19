"""
Clients to:
    - Rate a past appointment with clown face emojis

Clowns to:
- View their appointments and change the current status of these appointments
- Report an issue with an appointment (not a state change)
- Request client contact details, with a reason for the request
"""

from rest_framework.permissions import BasePermission


class IsTroupeLeader(BasePermission):
    message = 'Only troupe leaders can create appointments'

    def has_permission(self, request, view):
        return request.user.is_troupe_leader


class CanRatePastAppointment(BasePermission):
    message = 'only clients can rate appointments'

    def has_permission(self, request, view):
        return request.user.is_client


class IsAClown(BasePermission):
    message = 'only clowns can do this.'

    def has_permission(self, request, view):
        return request.data.is_clown
