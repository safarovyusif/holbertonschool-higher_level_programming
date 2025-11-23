import http.server
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Bu sinif HTTP sorğularını emal etmək üçün yaradılıb.
    BaseHTTPRequestHandler-dən miras alır.
    """

    def do_GET(self):
        """
        Bütün GET sorğuları bu metod tərəfindən idarə olunur.
        Biz self.path (URL yolu) əsasında qərar veririk.
        """
        
        # 1. Ana səhifə (Root endpoint)
        if self.path == '/':
            self.send_response(200) # Status kodu: OK
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            # wfile.write yalnız bayt (byte) qəbul edir, ona görə b"" və ya .encode() istifadə edirik
            self.wfile.write(b"Hello, this is a simple API!")

        # 2. Data endpointi (JSON qaytarır)
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Python lüğətini (dict) JSON formatına çeviririk
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            
            self.wfile.write(json_data.encode('utf-8'))

        # 3. Status endpointi
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
            
        # 4. Info endpointi (Gözlənilən nəticə hissəsində qeyd olunub)
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info_data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info_data).encode('utf-8'))

        # 5. Tapılmayan səhifələr (404 Error Handling)
        else:
            self.send_response(404) # Status kodu: Not Found
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run(server_class=http.server.HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """
    Serveri işə salan funksiya.
    """
    server_address = ('', port) # '' bütün IP-lərdən gələn sorğulara açıq deməkdir
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
