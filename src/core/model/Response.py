
class Headers:

    def __init__(self, content_type = 'application/json', **kwargs):
        self.__data = {}
        self.content_type = content_type
        self.__init_header()

    def __init_header(self):
        self.__data.update({'Content-Type' :self.content_type})

    def get_headers(self):
        return self.__data
class Response:

    def __init__(self, message='', code = 200, body=None, headers=Headers()):
        self.message = message
        self.code = code
        self.body = body
        self.headers = headers

    def get_response(self):
        to_send = dict()

        if self.message:
            to_send.update({'message': self.message})
        if self.body:
            to_send.update({'body': self.body})
        to_send.update({'code': self.code})
        to_send.update({'headers': self.headers})
        return to_send
