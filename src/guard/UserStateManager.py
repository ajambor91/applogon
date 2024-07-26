class UserStateManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserStateManager, cls).__new__(cls)
            cls._instance._current_user = None
        return cls._instance

    @property
    def current_user(self):
        return self._current_user

    @current_user.setter
    def current_user(self, user):
        self._current_user = user
