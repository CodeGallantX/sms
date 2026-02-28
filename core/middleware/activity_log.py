import logging

logger = logging.getLogger(__name__)

class ActivityLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            logger.info(f"User {request.user.email} accessed {request.path}")
        response = self.get_response(request)
        return response
