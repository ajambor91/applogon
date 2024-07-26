from src.classes.Crypto import Crypto
class Page:
    def __init__(self, link, login_field, password_field, domain):
        self.__crypto = Crypto()
        self.domain = domain
        self.link = link
        self.login_field = login_field
        self.password_field = password_field

        self.encrypted_domain = self.__crypto.encrypt(self.domain)
        self.encrypted_link = self.__crypto.encrypt(self.link)
        self.encrypted_login_field = self.__crypto.encrypt(self.login_field)
        self.encrypted_password_field = self.__crypto.encrypt(self.password_field)

