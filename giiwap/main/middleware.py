import datetime

class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Aquí haces logging simple
        if request.path != '/admin/':
            print(f"Visit: {request.path} - {datetime.datetime.now()} - IP: {request.META.get('REMOTE_ADDR')}")

        return response