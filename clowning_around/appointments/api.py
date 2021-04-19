from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from clowning_around.appointments.custom_permissions import IsTroupeLeader, IsAClown
from clowning_around.appointments.models import Appointment, Rating, Issue, ClientContactRequest
from clowning_around.appointments.serializers import AppointmentSerializer, IssueSerializer, \
    RatingSerializer
from clowning_around.users.models import Clown, Client
from clowning_around.users.serializers import ClownSerializer, ClientSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    permission_classes_by_action = {'create': [IsTroupeLeader],
                                    'default': [IsAuthenticated],
                                    'put': [IsAClown]}

    def get_permissions(self):
        try:
            # return permission_classes depending on 'action'
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes_by_action['default']]

    @action(detail=True)
    def get_upcoming_appointments(self, request):
        appointments = Appointment.objects.filter(status='1')
        serializer = self.get_serializer(appointments, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def get_past_appointments(self, request):
        appointments = Appointment.objects.filter(status="3")
        serializer = self.serializer_class(appointments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def report_issue(self, request, pk=None):
        if request.user.is_clown:
            appointment = get_object_or_404(self.queryset, pk=pk)
            issue = Issue(appointment=appointment)
            serializer = IssueSerializer(issue, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'response': "You don't have the permission to report an issue. You must be logged in "
                                     "as a clown"})

    @action(detail=True, methods=['post'])
    def rate_past_appointment(self, request, pk=None):
        if request.user.is_client:
            past_appointments = Appointment.objects.filter(status="3")
            appointment = get_object_or_404(past_appointments, pk=pk)
            rating = Rating(appointment=appointment)
            serializer = RatingSerializer(rating, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'response': "You don't have the permission to rate an appointment. You must be logged in as "
                                     "a client"})


class ClownViewSet(viewsets.ModelViewSet):
    queryset = Clown.objects.all()
    serializer_class = ClownSerializer

    @action(detail=True, methods=['post'])
    def request_client_details(self, request):
        if request.user.is_clown:

            data = JSONParser().parse(request)
            client = Client.objects.filter(contact_name=data['client_name'])
            client_data_serializer = ClientSerializer(client, many=True)
            client_contact_request = ClientContactRequest(client_name=data['client_name'], reason=data['reason'])
            client_contact_request.save()
            return Response(client_data_serializer.data)
        return Response({'response': "You don't have the permission to request client details. You must be logged in "
                                     "as a clown"})


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    # Bonus endpoint: Returning all the issues of a specific appointment.
    # As the list endpoint will return all issues of all appointments
    @action(detail=True)
    def get_all_issues_of_an_appointment(self, request, pk=None):
        """
        :param request:
        :param pk: appointment id
        :return:
        """
        appointment = Appointment.objects.get(pk=pk)
        appointment_issues = []
        all_issues = Issue.objects.all()

        for issue in all_issues:
            if issue.appointment.id == appointment.id:
                appointment_issues.append(issue)
        serializer = IssueSerializer(appointment_issues, many=True)
        return Response(serializer.data)


# Bonus endpoint: Returning all the ratings of a specific appointment.
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    @action(detail=True)
    def get_all_ratings_of_an_appointment(self, request, pk=None):
        appointment = Appointment.objects.get(pk=pk)
        appointment_ratings = []
        all_ratings = Rating.objects.all()

        for rating in all_ratings:
            if rating.appointment.id == appointment.id:
                appointment_ratings.append(rating)
        serializer = RatingSerializer(appointment_ratings, many=True)
        return Response(serializer.data)
