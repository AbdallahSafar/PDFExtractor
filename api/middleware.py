from django.http import JsonResponse
from django.conf import settings
from decouple import config

class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Load API Key auth variables
        API_KEY_NAME = config('API_KEY_NAME', default='default-header-key')
        API_SECRET_KEY = config('API_SECRET_KEY', default='default-secret-key')

        # Only protect paths that start with /api/
        if request.path.startswith('/api/'):
            api_key = request.headers.get(API_KEY_NAME)
            if api_key != API_SECRET_KEY:
                return JsonResponse({"error": "Unauthorized"}, status=401)
        return self.get_response(request)
