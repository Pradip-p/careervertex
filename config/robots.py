from django.http import HttpResponse
from django.views.generic import View


class RobotsTxtView(View):
    def get(self, request, *args, **kwargs):
        # Allow all by default
        content = "User-agent: *\nDisallow: /contact-us/"

        # Disallow the contact-us page
        if request.path == '/contact-us/':
            content = "User-agent: *\nDisallow: /contact-us/"

        return HttpResponse(content, content_type="text/plain")