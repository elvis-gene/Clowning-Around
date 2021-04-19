from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from clowning_around.appointments.api import AppointmentViewSet, ClownViewSet, IssueViewSet, RatingViewSet

app_name = "appointments"

# could be used for get methods: renderer_classes=[renderers.StaticHTMLRenderer]
appointment_list = AppointmentViewSet.as_view({
    'get': 'list',
})
create_appointment = AppointmentViewSet.as_view({
    'post': 'create',
    'get': 'list'
})
appointment_detail = AppointmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
upcoming_appointments = AppointmentViewSet.as_view({
    'get': 'get_upcoming_appointments'
})
past_appointments = AppointmentViewSet.as_view({
    'get': 'get_past_appointments'
})
report_an_issue = AppointmentViewSet.as_view({
    'post': 'report_issue',
    'get': 'retrieve'
})
update_appointment = AppointmentViewSet.as_view({
    'put': 'update',
    'get': 'retrieve'
})
rate_past_appointment = AppointmentViewSet.as_view({
    'post': 'rate_past_appointment'
})
list_appointment_issues = IssueViewSet.as_view({
    'get': 'list'
})
list_appointment_ratings = RatingViewSet.as_view({
    'get': 'list'
})
get_an_appointment_issues = IssueViewSet.as_view({
    'get': 'get_all_issues_of_an_appointment'
})
get_an_appointment_ratings = RatingViewSet.as_view({
    'get': 'get_all_ratings_of_an_appointment'
})
request_client_details = ClownViewSet.as_view({
    'post': 'request_client_details'
})

urlpatterns = format_suffix_patterns([
    path('', appointment_list),
    path('appointment/<int:pk>/', appointment_detail),
    path('get_upcoming_appointments/', upcoming_appointments),
    path('get_past_appointments/', past_appointments),
    path('create/', create_appointment),
    path('<int:pk>/report_issue/', report_an_issue),
    path('<int:pk>/update/', update_appointment),
    path('<int:pk>/rate_appointment/', rate_past_appointment),
    path('appointment_issues/', list_appointment_issues),
    path('appointment_ratings/', list_appointment_ratings),
    path('<int:pk>/get_an_appointment_ratings/', get_an_appointment_ratings),
    path('<int:pk>/get_an_appoinmtent_issues/', get_an_appointment_issues),
    path('request_client_details/', request_client_details),
    path('emoji/', include('emoji.urls')),
])

# To read emoji names:
# http://127.0.0.1:8000/appointments/emoji/all.json
