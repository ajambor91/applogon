from src.entities.User import User
from src.db.DataBase import DataBase
from src.functions.db import entity
class UserRepo:

    def __init__(self):
        self.conn = DataBase()

    @entity
    def insert_user(self, user: User):

        try:
            cursor = self.conn.db_connect()
            cursor.execute('''INSERT INTO user (login, password)
                            VALUES (?, ?)''', (user.login, user.password))
            user = User(login=user.login)
            return user
        except:
            return False
    @entity
    def get_user(self, user: User):
        try:
            cursor = self.conn.db_connect()
            cursor.execute('''SELECT login, password FROM user WHERE login = ? AND password = ? ''', (user.login, user.password))
            result = cursor.fetchone()
            user = User(login = result[0])
            return user
        except:
            return False

    @entity
    def upddate_user(self, user: User):
        try:
            cursor = self.conn.db_connect()
            cursor.execute('''UPDATE user SET session_id = ? WHERE login = ? AND password = ?''',
                       (user.session_id, user.login, user.password))
            result = cursor.fetchone()
            user = User(login=user)
            return user
        except:

            return False