from src.entities.User import User
from src.db.DataBase import DataBase
from src.core.functions.db import entity
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
        except Exception as e:
            return False
    @entity
    def get_user(self, user: User):
        try:
            cursor = self.conn.db_connect()
            cursor.execute('''SELECT login, password FROM user WHERE login = ? AND password = ? ''', (user.login, user.password))
            result = cursor.fetchone()
            user = User(login = result[0])
            return user
        except Exception as e:
            return False

    @entity
    def upddate_user(self, user: User):
        try:
            cursor = self.conn.db_connect()
            cursor.execute('''UPDATE user SET jwt_token = ? WHERE login = ? AND password = ?''',
                       (user.jwt_token, user.login, user.password))
            result = cursor.fetchone()
            user = User(login=user, jwt_token=user.jwt_token)
            return user
        except Exception as e:
            return False

    @entity
    def get_user_by_jwt(self, jwt):
        try:
            cursor = self.conn.db_connect()
            cursor.execute('''SELECT user.login, user.jwt_token FROM user WHERE jwt_token = ? ''',
                       (jwt,))
            result = cursor.fetchone()
            if result is not None:
                return User(login = result[0], jwt_token=result[1])
            else:
                return False
        except Exception as e:
            return False