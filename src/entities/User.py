import hashlib

class User:
    def __init__(self, login, password = None, session_id = None):
        self.__session_id = session_id
        self.__login = login
        self.__password = self.__hash_pass(password) if password is not None else None

    def __hash_pass(self, password):
        p_bytes = password.encode('utf-8')
        return  hashlib.sha224(p_bytes).hexdigest()


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, current_password):
        self.__password = self.__hash_pass(current_password)

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, current_login):
        self.__login = current_login

    @property
    def session_id(self):
        return self.__session_id

    @session_id.setter
    def session_id(self, current_session_id):
        self.__session_id = current_session_id

    def set_password(self, password):
        self.password = self.__hash_pass(password)
        return self
    def set_session_id(self, session_id):
        self.session_id = session_id
        return self
    def set_login(self, session_id):
        self.session_id = session_id
        return self

    def get_data(self):
        return {"login": self.__login, "password": self.__password, 'session_id': self.__session_id}