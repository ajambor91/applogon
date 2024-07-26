import functools
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler
import json
import re
import inspect
from src.model.Response import Response
def extract_params(input_string):
    pattern = r'(\w+):([^/]+)'
    matches = re.findall(pattern, input_string)
    params_dict = {key: value for key, value in matches}
    return params_dict


def get(url, params = None, guard = None):
    def decorate(func):
        mapped_params = extract_params(params) if params is not None else None
        setattr(func, '_route', url)

        setattr(func, '__url__', url)
        setattr(func, '__params__', mapped_params)
        setattr(func, '__http_method__', 'GET')
        setattr(func, '__guard__', guard if guard is not None else None)


        @functools.wraps(func)
        def wrapper(instance, *args, **kwargs):
            return func(instance, *args, **kwargs)

        return wrapper

    return decorate


def post(url, params = None, guard = None):
    def decorate(func):
        setattr(func, '_route', url)
        mapped_params = extract_params(params) if params is not None else None
        setattr(func, '__url__', url)
        setattr(func, '__params__', mapped_params)
        setattr(func, '__http_method__', 'POST')
        setattr(func, '__guard__', guard if guard is not None else None)

        @functools.wraps(func)
        def wrapper(instance, *args, **kwargs):
            return func(instance, *args, **kwargs)

        return wrapper

    return decorate


def controller(url, guard = None):
    def decorate(cls):
        setattr(cls, '__url__', url)
        setattr(cls, '__guard__', guard if guard is not None else None)
        class NewClass(cls):
            routes = []
            arrpath = None
            def __init__(self, server, arrpath):
                cls.__init__(self)
                self.arrpath = arrpath
                self.server = server
                self.guard = getattr(self, '__guard__')
                self.route = getattr(self, '__url__')



        return NewClass

    return decorate
