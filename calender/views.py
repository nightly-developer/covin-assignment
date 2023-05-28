from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.auth.transport import requests

# Constants for Google OAuth2
CLIENT_ID = '89335088404-0vgojdriovtf1psnco7v150468u4fs09.apps.googleusercontent.com'
CLIENT_SECRET = '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'
REDIRECT_URI = 'http://localhost:8000/rest/v1/calendar/redirect/'
SCOPES = ['https://www.googleapis.com/auth/calendar']

class GoogleCalendarInitView(View):
    def get(self, request):
        flow = Flow.from_client_secrets_file(
            'calender/client_secret.json',
            scopes=SCOPES,
            redirect_uri=REDIRECT_URI
        )
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )
        request.session['oauth2_state'] = state
        return HttpResponseRedirect(authorization_url)