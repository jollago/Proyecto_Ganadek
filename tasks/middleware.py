from django.shortcuts import redirect
from django.urls import reverse, NoReverseMatch

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        try:
            self.exclude_urls = [
                reverse('signin'),     # tu vista de inicio de sesión
                '/admin/login/',
                '/admin/',
                '/static/',
            ]
        except NoReverseMatch:
            self.exclude_urls = [
                '/signin/',
                '/admin/login/',
                '/admin/',
                '/static/',
            ]

    def __call__(self, request):
        if not request.user.is_authenticated:
            if not any(request.path.startswith(url) for url in self.exclude_urls):
                return redirect(f'/signin/?next={request.path}')
        return self.get_response(request)
