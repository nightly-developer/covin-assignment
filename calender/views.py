from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import View
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