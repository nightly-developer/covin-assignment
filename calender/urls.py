from django.urls import path
from . import views
from .views import GoogleCalendarInitView,GoogleCalendarRedirectView

urlpatterns = [
    # path('', views.home, name='home'),
    path('rest/v1/calendar/init/', GoogleCalendarInitView.as_view(), name='google_calendar_init'),
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView.as_view(), name='google_calendar_redirect'),
]