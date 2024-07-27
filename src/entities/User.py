import hashlib

class User:
    def __init__(self, login, password = None, session_id = None, jwt_token=None):
        self.session_id = session_id
        self.login = login
        self.jwt_token = jwt_token
        self.password = self.__hash_pass(password) if password is not None else None

    def __hash_pass(self, password):
        p_bytes = password.encode('utf-8')
        return  hashlib.sha224(p_bytes).hexdigest()
