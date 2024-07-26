import os.path
from src.config import HOME_PATH
from cryptography.fernet import Fernet

class Crypto:
    def __init__(self):
        self.key = self.__get_crypto_key()
        self.fernet = Fernet(self.key)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Crypto,cls).__new__(cls)
        return cls.instance
    def __get_crypto_key(self):
        f = open(os.path.join(HOME_PATH, 'conf'),'rb')
        return f.read()

    def encrypt(self, data):
        return self.fernet.encrypt(data.encode('utf-8'))

    def decrypt(self, data):
        return self.fernet.decrypt(data).decode('utf-8')