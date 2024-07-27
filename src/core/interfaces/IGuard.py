from http.server import BaseHTTPRequestHandler


class IGuard:
    def guard(self, request: BaseHTTPRequestHandler) -> bool:
        pass
