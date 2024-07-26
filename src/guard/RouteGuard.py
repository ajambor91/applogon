from src.guard.UserAuthService import UserAuthService
class RouteGuard(object):



    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RouteGuard, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.user_auth = UserAuthService()

    def guard(self, session_id):
        user = self.user_auth.get_user()
        return True if hasattr(user, 'session_id') and user.session_id == session_id else False