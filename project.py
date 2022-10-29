import requests
from http.server import HTTPServer,BaseHTTPRequestHandler
HOST = "172.20.10.6"
PORT = 9999

class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Conect-type","text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>AviaSTAR </h1> <h1> air tickets </h1></body></html>","utf-8"))
        self.wfile.write(bytes("<html><body><h1>AviaSTAR </h1> <h1> air tickets </h1></body></html>","utf-8"))


server = HTTPServer((HOST,PORT),NeuralHTTP)
print("Server is working")

server.serve_forever()
server.server_close()

print("Server stopped")                   
            




