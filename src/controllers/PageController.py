from src.functions.rest_api import controller, get
from src.repos.PageRepo import PageRepo
from src.entities.Page import Page
from src.model.Response import Response
from src.guard.RouteGuard import RouteGuard
@controller('/')
class PageController:

    def __init__(self):
        self.repo = PageRepo()

    @get('/')
    def test(self):
        self.repo = PageRepo()

        self.repo.insert_page(Page(link='test', data='data'))
        return Response('sadsdLogin', 404)
    @get('/get', guard=RouteGuard)
    def testX(self):
        self.repo = PageRepo()

        records = self.repo.get_pages()
        return Response('dddd', 200, body=records)