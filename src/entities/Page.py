from src.classes.Crypto import Crypto
class Page:
    def __init__(self, domain,link = None, login_field = None, password_field = None):
        self.__crypto = Crypto()
        self.domain = domain
        self.link = link
        self.login_field = login_field
        self.password_field = password_field

        self.encrypted_domain = self.__crypto.encrypt(self.domain)
        self.encrypted_link = self.__crypto.encrypt(self.link)
        self.encrypted_login_field = self.__crypto.encrypt(self.login_field)
        self.encrypted_password_field = self.__crypto.encrypt(self.password_field)
        self.hashed_domain = self.__crypto.hash(self.domain)

