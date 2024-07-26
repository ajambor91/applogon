from src.functions.rest_api import controller, get
from src.repos.PageRepo import PageRepo
from src.entities.Page import Page
from src.model.Response import Response
from src.guard.RouteGuard import RouteGuard

from src.functions.rest_api import post


@controller('/')
class PageController:

    def __init__(self):
        self.repo = PageRepo()

    @post('/insert')
    def test(self):
        self.repo = PageRepo()

        self.repo.insert_page(Page(link='test', login_field='data', password_field='datd', domain='dsadsd'))
        return Response('sadsdLogin', 404)
    @get('/get', guard=RouteGuard)
    def testX(self):
        self.repo = PageRepo()

        records = self.repo.get_pages()[0].decrypted_domain
        return Response('dddd', 200, body=records)