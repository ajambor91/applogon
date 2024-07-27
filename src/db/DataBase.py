import sqlite3
class DataBase(object):

    def __init__(self):
        self.__check_table()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DataBase, cls).__new__(cls)
        return cls.instance

    def db_connect(self):
        self.conn = sqlite3.connect('passwords_py.db')
        cursor = self.conn.cursor()
        return cursor

    def db_disconnect(self):
        self.conn.commit()
        self.conn.close()

    def __create_table(self, cursor):
        cursor.execute('''CREATE TABLE IF NOT EXISTS pages (
                               id INTEGER PRIMARY KEY,
                               login_field TEXT,
                               password_field TEXT,
                               domain TEXT, 
                               link TEXT,
                               hashed_domain TEXT
                           )''')

    def __create_table_user(self, cursor):
        cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                               id INTEGER PRIMARY KEY,
                               login TEXT,
                               password TEXT,
                               jwt_token TEXT
                           )''')
    def __check_table(self):
        try:
            cursor = self.db_connect()
            self.__create_table(cursor)
            self.__create_table_user(cursor)
        except sqlite3.Error as e:
            print('EXCEPTION',e)
