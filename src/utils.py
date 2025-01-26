from http.server import BaseHTTPRequestHandler
from pathlib import Path


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        html_dir = Path(__file__).parent.parent.joinpath('pages')
        file_path = html_dir / "contacts.html"

        if file_path.exists():
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            return self.wfile.write(content.encode("utf-8"))
        else:
            return self.send_error(404, "HTML Страница не найдена")
