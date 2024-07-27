from http.server import BaseHTTPRequestHandler

from src.guard.UserAuthService import UserAuthService

from src.core.interfaces.IGuard import IGuard


class AuthGuard(IGuard):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AuthGuard, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.user_auth = UserAuthService()

    def __get_auth_headers(self, request):
        return request.headers.get('Authorization')
    def guard(self, request: BaseHTTPRequestHandler):
        user = self.user_auth.is_login(self.__get_auth_headers(request))
        print('USSS',user)
        return True if user is not None and user is not False else False
