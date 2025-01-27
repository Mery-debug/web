from http.server import HTTPServer
from src.utils import MyServer


hostName = "localhost"
serverPort = 8080


def point_start(server_class=HTTPServer, handler_class=MyServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on port {port}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("Server stopped")


if __name__ == "__main__":
    point_start()
