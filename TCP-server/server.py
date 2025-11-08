import socket

def parse_http_request(request_data: str) -> dict:
    '''Парсит HTTP запрос на составные части'''
    lines = request_data.split('\r\n')
    if not lines or not lines[0]:
        return None
    method, path, version = lines[0].split()
    headers = {}
    body = None
    for i in range(1, len(lines)):
        if lines[i] == '':
            if i + 1 < len(lines):
                body = '\r\n'.join(lines[i+1:])
            break
        if ': ' in lines[i]:
            key, value = lines[i].split(': ', 1)
            headers[key] = value
    return {
        'method': method,
        'path': path,
        'version': version,
        'headers': headers,
        'body': body
    }

def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9090))
    server_socket.listen(5)
    server_socket.settimeout(1.0) 
    print('TCP Server started on localhost:9090')
    try:
        while True:
            client_socket = None
            client_address = None
            try:
                client_socket, client_address = server_socket.accept()
                print(f'Client connected: {client_address}')
                request_data = client_socket.recv(4096).decode('utf-8')
                print(f'Received HTTP request from {client_address}')
                parsed_request = parse_http_request(request_data)
                if parsed_request:
                    response_text = f'''HTTP Request Parsed Successfully:
Method: {parsed_request['method']}
Path: {parsed_request['path']}
Version: {parsed_request['version']}
Headers:
                    '''
                    for key, value in parsed_request['headers'].items():
                        response_text += f'{key}: {value}\n'
                    if parsed_request['body']:
                        response_text += f'\nBody:\n{parsed_request['body']}\n'
                    else:
                        response_text += '\nBody: None\n'
                    response_text += f'\nClient: {client_address[0]}:{client_address[1]}'
                else:
                    response_text = 'Error: Invalid HTTP request format'
                http_response = f'''HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: {len(response_text)}
Connection: close
                {response_text}'''
                client_socket.send(http_response.encode('utf-8'))
                print(f'Response sent to {client_address}')
            except socket.timeout:
                continue  
            except Exception as e:
                print(f'Error handling client: {e}')
                error_response = 'HTTP/1.1 500 Internal Server Error\r\n\r\nServer Error'
                if client_socket:
                    client_socket.send(error_response.encode('utf-8'))
            finally:
                if client_socket:
                    client_socket.close()
                    print(f'Connection closed with {client_address}\n')
    except KeyboardInterrupt:
        print('\nServer stopped by user')
    finally:
        server_socket.close()
        print('Server socket closed')

if __name__ == '__main__':
    start_tcp_server()