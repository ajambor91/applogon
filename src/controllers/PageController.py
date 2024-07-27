from src.core.functions.rest_api import controller, get
from src.repos.PageRepo import PageRepo
from src.entities.Page import Page
from src.core.model.Response import Response
from src.guard.AuthGuard import AuthGuard

from src.core.functions.rest_api import post


@controller('/')
class PageController:

    def __init__(self):
        self.repo = PageRepo()

    @post('/insert')
    def test(self, **kwargs):
        self.repo = PageRepo()
        self.repo.insert_page(Page(link='test', login_field='data', password_field='datd', domain='domena'))
        return Response('sadsdLogin', 404)
    @get('/get', guard=AuthGuard)
    def testX(self):
        self.repo = PageRepo()
        records = self.repo.get_pages()[0].decrypted_domain
        return Response('dddd', 200, body='aaaaa')

    @get('/get/:domain')
    def testk(self, domain):
        self.repo = PageRepo()
        page = Page(domain=domain)
        record = self.repo.get_page(page)
        return Response('dddd', 200, body=record.decrypted_password_field)