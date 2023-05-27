from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import View
from google.auth.transport import requests
from django.contrib import messages


# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# endpoints and credentials
CLIENT_ID = '89335088404-0vgojdriovtf1psnco7v150468u4fs09.apps.googleusercontent.com'
CLIENT_SECRET = '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'
REDIRECT_URI = 'http://localhost:8000/rest/v1/calendar/redirect/'
SCOPE = 'https://www.googleapis.com/auth/calendar.readonly'

# prompt user for his/her credentials
class GoogleCalendarInitView(View):
    def get(self, request):
        # Redirect user to Google for authentication
        auth_url = f'https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}&response_type=code'
        return HttpResponseRedirect(auth_url)
    
class GoogleCalendarRedirectView(View):
    def get(self, request):
        # Retrieve the authorization code from the redirect URL
        code = request.GET.get('code')

        # Exchange authorization code for access token
        token_url = 'https://accounts.google.com/o/oauth2/token'
        token_data = {
            'code': code,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': REDIRECT_URI,
            'grant_type': 'authorization_code'
        }
        response = requests.post(token_url, data=token_data)

        if response.status_code == 200:
            # Get access token from the response
            access_token = response.json().get('access_token')

            # Retrieveing calendar events
            events_url = 'https://www.googleapis.com/calendar/v3/calendars/primary/events'
            headers = {'Authorization': f'Bearer {access_token}'}
            events_response = requests.get(events_url, headers=headers)

        else:
            return HttpResponse('Failed to exchange authorization code for access token', status=response.status_code)