import importlib.util
import inspect
import json
import os
from http.server import BaseHTTPRequestHandler
from src.classes.Route import Route

from glob import glob
from src.config import ROOT_DIR

class Router(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        self.__current_http_method = None
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.routes = []
        instance.__controllers_dir = os.path.join(ROOT_DIR, 'controllers')
        instance.__get_controllers()
        return instance

    def __get_controllers(self):

        for file in glob(os.path.join(ROOT_DIR, 'src', 'controllers', '*.py')):
            name = os.path.splitext(os.path.basename(file))[0]
            full_path = os.path.join(self.__controllers_dir, file)
            spec = importlib.util.spec_from_file_location(name, full_path)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                self.__get_decorators(module)
            else:

    def __get_decorators(self, module):
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if inspect.isclass(attr):
                if hasattr(attr, '__url__'):
                    base_path = getattr(attr, '__url__')
                    for method_name, method in inspect.getmembers(attr, predicate=inspect.isfunction):
                        if hasattr(method, '__url__'):
                            full_path = base_path.rstrip('/') + '/' + getattr(method, '__url__').lstrip('/')
                            self.routes.append(Route(path=full_path, http_method=getattr(method, '__http_method__'), controller=attr,action= method_name, guard=getattr(method,'__guard__')))

    def route(self, path, method):

        for route in self.routes:
            if route.match(path) and route.http_method == method:
                return route
        return None

    def do_POST(self):
        self.__handle_request('POST')

    def do_GET(self):
        self.__handle_request('GET')

    def __handle_request(self, method):
        route = self.route(self.path, method)
        if route and route.guard is None or route.guard and route.guard.guard('sjdhakujfgejhfg'):
            controller_instance = route.controller(self.server, self.path.split('/'))
            action = getattr(controller_instance, route.action)
            response = action()
            self.send_response(response.get_response().get('code'))
            headers = response.get_response().get('headers').get_headers().items()
            for header in headers:
                self.send_header(header[0], header[1])
            self.end_headers()

            body = {
                "message": response.get_response().get('body')
            }
            body.update({"body": response.get_response().get('message')})
            self.wfile.write(json.dumps(body).encode('utf-8'))
        elif route.guard and route.guard.guard('sjdhakujfgejhfg') is not True:
            self.send_error(403, "Forbidden")
        else:
            self.send_error(404, "Not Found")
