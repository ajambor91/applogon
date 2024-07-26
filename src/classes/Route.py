# route.py
import re


class Route:
    def __init__(self, path, http_method, controller, action, guard):
        self.path = path
        self.http_method = http_method
        self.controller = controller
        self.action = action
        self.guard = guard() if guard is not None else None
        self.pattern = self.__compile_pattern(path)


    def __compile_pattern(self, path):
        pattern = re.sub(r':(\w+)', r'(?P<\1>[^/]+)', path)
        pattern = f'^{pattern}$'
        return re.compile(pattern)

    def match(self, path):
        return self.pattern.match(path)

    def __repr__(self):
        return f'Route(path={self.path}, method={self.http_method}, controller={self.controller.__name__}, action={self.action})'
