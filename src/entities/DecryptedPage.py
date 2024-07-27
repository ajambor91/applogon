from src.core.classes.Crypto import Crypto
class DecryptedPage:
    def __init__(self, link, login_field, password_field, domain):
        self.__crypto = Crypto()
        self.domain = domain
        self.link = link
        self.login_field = login_field
        self.password_field = password_field

        self.decrypted_domain = self.__crypto.decrypt(self.domain)
        self.decrypted_link = self.__crypto.decrypt(self.link)
        self.decrypted_login_field = self.__crypto.decrypt(self.login_field)
        self.decrypted_password_field = self.__crypto.decrypt(self.password_field)

