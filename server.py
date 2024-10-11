from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import json

HOST = "127.0.0.1"
PORT = 8080

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>GET Request Handled</h1></body></html>")
    
    def do_POST(self):
        # Properly handle the POST request and return a JSON response
        content_length = int(self.headers['Content-Length'])  # Get the length of data
        post_data = self.rfile.read(content_length)  # Read the data
        print(f"Received POST data: {post_data.decode('utf-8')}")

        # Respond with the current timestamp in JSON format
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = {
            "message": "POST request handled successfully",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
        self.wfile.write(json.dumps(response).encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"Server running on {HOST}:{PORT}")
    server.serve_forever()
