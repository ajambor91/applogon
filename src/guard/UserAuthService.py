from src.repos.UserRepo import UserRepo
from src.entities.User import User
from src.guard.UserStateManager import UserStateManager
import jwt
class UserAuthService(object):
    def __init__(self):
        self.__user_state = UserStateManager()
        self.__user_repo = UserRepo()
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(UserAuthService, cls).__new__(cls)
        return cls.instance

    def login(self, login, password):
        poss_user = User(login, password)
        user = self.__user_repo.get_user(poss_user)
        self.__user_state.current_user = user
        self.__set_jwt(poss_user)
        user = self.get_user()

        return user if user is not None else False

    def is_login(self, jwt):
        if jwt is None:
            return False
        if self.__user_state.current_user is not None and hasattr(self.__user_state.current_user, 'jwt_token') and self.__user_state.current_user.jwt_token == jwt:
            print('DEBUG 1')
            return self.__user_state.current_user
        else:
            user = self.__user_repo.get_user_by_jwt(jwt)
            if user is not None:
                print('DEBUG 2')

                self.__user_state.current_user = user
                return User
            else:
                return False

    def register(self,  login, password):

        poss_user = User(login, password)
        user = self.__user_repo.insert_user(poss_user)
        return user if user is not None else False

    def get_user(self):
        return self.__user_state.current_user

    def __set_jwt(self,poss_user):
        jwt_token = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
        poss_user.jwt_token = jwt_token
        self.__user_repo.upddate_user(poss_user)
