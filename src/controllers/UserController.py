from src.functions.rest_api import controller, get, post
from src.guard.UserAuthService import UserAuthService
from src.guard.RouteGuard import RouteGuard
from src.entities.User import User
from src.model.Response import Response
@controller('/user', guard=RouteGuard)
class UserController:

    def __init__(self):

        self.auth_service = UserAuthService()

    @post('/insert')
    def insert(self):
        self.auth_service = UserAuthService()
        user = self.auth_service.register(login='test', password='data')

        return Response('Insert', 200)

    @post('/login/:id')
    def test(self):

        self.auth_service = UserAuthService()
        user = self.auth_service.login(login='test', password='data', session_id='sjdhakujfgejhfg')
        return Response('Login', 404)