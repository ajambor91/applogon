import os.path
from http.server import HTTPServer
from src.db.DataBase import DataBase

from src.src.core.classes.Crypto import Crypto
from src.src.core.classes.Router import Router
from src.config import HOME_PATH
from cryptography.fernet import Fernet

class App:
    def __init__(self):
        self.__start()

    def __start(self):
        self.__check_is_first_start()
        self.__db_run()
        self.__start_crypto()
        self.__run_server()


    def __check_is_first_start(self):
        if os.path.exists(HOME_PATH) and os.path.exists(os.path.join(HOME_PATH,'conf')):
            return True
        else:
            self.__create_app_conf()

    def __run_server(self,server_class=HTTPServer, port=8000):
            server_address = ('', port)
            httpd = server_class(server_address, Router)
            httpd.serve_forever()
    def __db_run(self):
        db = DataBase()

    def __create_app_conf(self):
        if not os.path.exists(HOME_PATH):
            os.mkdir(HOME_PATH)
        if os.path.exists(HOME_PATH):
            f = open(os.path.join(HOME_PATH, 'conf'),'a')
            f.close()
        if  os.path.exists(os.path.join(HOME_PATH,'conf')):
            f = open(os.path.join(HOME_PATH, 'conf'),'wb')
            bytes_var = Fernet.generate_key()
            f.write(bytes_var)
            f.close()

    def __start_crypto(self):
        crypto = Crypto()