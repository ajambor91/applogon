from http.server import HTTPServer
from src.db.DataBase import DataBase
from src.src.classes.Router import Router


class App:
    def __init__(self):
        self.__run()
        self.__db_run()

    def __run(self,server_class=HTTPServer, port=8000):
            server_address = ('', port)
            httpd = server_class(server_address, Router)
            httpd.serve_forever()
    def __db_run(self):
        db = DataBase()
