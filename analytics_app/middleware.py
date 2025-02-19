from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponsePermanentRedirect
import urllib.parse

class URLNormalizationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if '%0A' in request.path_info or '%0a' in request.path_info:
            # Remove newline characters and normalize the URL
            clean_path = request.path_info.replace('%0A', '').replace('%0a', '').rstrip('/')
            # Ensure the path starts with /
            if not clean_path.startswith('/'):
                clean_path = f"/{clean_path}"
            # Preserve query parameters if any
            if request.META.get('QUERY_STRING'):
                clean_path = f"{clean_path}?{request.META['QUERY_STRING']}"
            return HttpResponsePermanentRedirect(clean_path)
        return None
