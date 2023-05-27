from django.urls import path
from . import views
from .views import GoogleCalendarInitView,GoogleCalendarRedirectView

urlpatterns = [
    path('', GoogleCalendarInitView.as_view(), name='google_calendar_init'),
    path('', GoogleCalendarRedirectView.as_view(), name='google_calendar_redirect'),
]