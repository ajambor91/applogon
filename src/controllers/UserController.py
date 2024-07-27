from src.core.functions.rest_api import controller, get, post
from src.guard.UserAuthService import UserAuthService
from src.guard.AuthGuard import AuthGuard
from src.core.model.Response import Response
@controller('/user', guard=AuthGuard)
class UserController:

    def __init__(self):

        self.auth_service = UserAuthService()

    @post('/insert')
    def insert(self):
        self.auth_service = UserAuthService()
        user = self.auth_service.register(login='test', password='data')

        return Response('Insert', 200)

    @post('/login')
    def test(self):

        self.auth_service = UserAuthService()
        user = self.auth_service.login(login='test', password='data')
        return Response('Login', 404)