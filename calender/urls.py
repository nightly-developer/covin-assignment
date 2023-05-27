from django.urls import path
from . import views
from .views import GoogleCalendarInitView

urlpatterns = [
    path('', GoogleCalendarInitView.as_view(), name='google_calendar_init'),
]