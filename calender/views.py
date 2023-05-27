from rest_framework.response import Response
from rest_framework.decorators import api_view

# endpoints and credentials
CLIENT_ID = '89335088404-0vgojdriovtf1psnco7v150468u4fs09.apps.googleusercontent.com'
CLIENT_SECRET = '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'
REDIRECT_URI = 'http://localhost:8000/rest/v1/calendar/redirect/'
SCOPE = 'https://www.googleapis.com/auth/calendar.readonly'

