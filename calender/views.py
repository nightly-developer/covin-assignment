from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.auth.transport import requests

# Constants for Google OAuth2
CLIENT_ID = ''
CLIENT_SECRET = ''
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
    
class GoogleCalendarRedirectView(View):
    def get(self, request):
        state = request.session.get('oauth2_state')
        if state is None :#or state != request.GET.get('state'):
            return HttpResponse('Invalid state parameter', status=400)
        
        flow = Flow.from_client_secrets_file(
            'calender/client_secret.json',  # Path to your client_secret.json file
            scopes=SCOPES,
            redirect_uri=REDIRECT_URI,
            state=state
        )
        flow.fetch_token(
            authorization_response=request.build_absolute_uri(),
            client_secret=CLIENT_SECRET
        )
        credentials = flow.credentials

        service = build('calendar', 'v3', credentials=credentials)
        events_result = service.events().list(calendarId='primary', maxResults=10).execute()
        events = events_result.get('items', [])

        #process Events
        
        return HttpResponse('Events fetched successfully')
