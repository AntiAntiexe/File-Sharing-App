from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import os
import http.server


def startWithIndex(HOST, PORT):

  class handler(BaseHTTPRequestHandler):

    def do_GET(self):
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()

      try:
        with open("index.html", "r", encoding="utf-8") as file:
          html_content = file.read()
        self.wfile.write(bytes(html_content, "utf-8"))
      except FileNotFoundError:
        self.wfile.write(b"<html><body><h1>404 Not Found</h1></body></html>")

  server = HTTPServer((HOST, PORT), handler)
  print("Server started")
  server.serve_forever()
  server.server_close()


def startWithFile(HOST, PORT, file_path):

  class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
      self.send_header('Access-Control-Allow-Origin', '*')
      super().end_headers()

  os.chdir(file_path)  # Change to the directory containing your files
  handler_object = MyHttpRequestHandler

  with socketserver.TCPServer((HOST, PORT), handler_object) as httpd:
    print(f'Serving at port {PORT}...')
    print("Server is running press Ctrl+C to stop")

    try:
      httpd.serve_forever()
    except KeyboardInterrupt:
      pass

    print("Server stopped")
    httpd.server_close()
    print("server closed")






