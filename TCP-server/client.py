import socket

def send_http_request(method='GET', path='/', headers=None, body=None):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 9090))
        print("Connected to server")
        default_headers = {
            'Host': 'localhost:9090',
            'User-Agent': 'Simple-Test-Client',
            'Connection': 'close'
        }
        if headers:
            default_headers.update(headers)
        if body:
            default_headers['Content-Length'] = str(len(body))
        request_line = f"{method} {path} HTTP/1.1\r\n"
        headers_section = ''.join([f'{key}: {value}\r\n' for key, value in default_headers.items()])
        http_request = request_line + headers_section + '\r\n'
        if body:
            http_request += body
        print(f"Sending {method} {path}")
        client_socket.send(http_request.encode())
        response = client_socket.recv(4096).decode()
        print("Response received:")
        print(response)
    except ConnectionRefusedError:
        print("Server is not running")
    finally:
        client_socket.close()

if __name__ == "__main__":
    send_http_request('GET', '/')
    send_http_request('GET', '/api/users')
    send_http_request('GET', '/about')
    send_http_request('POST', '/submit', 
                    body='name=John&age=30')
    send_http_request('GET', '/test', 
                    headers={'Authorization': 'Bearer token123', 'Accept': 'application/json'})