class PermissionsPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Permissions-Policy"] = 'fullscreen=(self "https://www.careervertex.com"),geolocation=*, camera=()'
        return response