import os
import http.server
import socketserver
import socket


class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('hello'.encode())
        elif self.path == '/hostname':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(socket.gethostname().encode())
        elif self.path == '/author':
            author = os.environ.get('AUTHOR', 'Unknown')
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(author.encode())
        elif self.path == '/id':
            uuid_value = os.environ.get('UUID', 'Unknown')
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(uuid_value.encode())
        else:
            self.send_error(404)


def run():
    port = 8000
    handler = RequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Server running on port {port}")
        httpd.serve_forever()


if __name__ == "__main__":
    run()
