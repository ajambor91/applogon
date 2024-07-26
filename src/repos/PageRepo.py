from src.entities.Page import Page
from src.db.DataBase import DataBase
from src.functions.db import entity

from src.entities.DecryptedPage import DecryptedPage


class PageRepo:

    def __init__(self):
        self.conn = DataBase()

    @entity
    def insert_page(self, page: Page):
        cursor = self.conn.db_connect()
        cursor.execute('''INSERT INTO pages (login_field, password_field, domain, link, hashed_domain)
                          VALUES (?, ?, ?, ?, ?)''', (page.encrypted_login_field, page.encrypted_password_field, page.encrypted_domain, page.encrypted_link, page.hashed_domain))

    @entity
    def get_pages(self):
        cursor = self.conn.db_connect()
        cursor.execute('''SELECT login_field, password_field, domain, link FROM pages''')
        result = cursor.fetchall()
        data = list(map(lambda item: DecryptedPage(
            login_field=item[0],
            password_field = item[1],
            domain = item[2],
            link = item[3]
        ), result))
        return data

    @entity
    def get_page(self, page):
        cursor = self.conn.db_connect()
        cursor.execute('''SELECT login_field, password_field, domain, link FROM pages WHERE hashed_domain = ? ''',(page.hashed_domain,))
        result = cursor.fetchone()

        data = DecryptedPage(
            login_field=result[0],
            password_field=result[1],
            domain=result[2],
            link=result[3]
        )
        return data