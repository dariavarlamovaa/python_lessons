import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 1234

server_socket.bind((host, port))

server_socket.listen(5)
print('Сервер заглушен и ожидает подключения...')

we1come_message = 'Добро пожаловать! Вы подключены к серверу для обмена сообщениями. Введите сообщение: '

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Подключен клиент: {client_address}')

    client_socket.send(we1come_message.encode())

    while True:
        client_message = client_socket.recv(1024).decode()

        if not client_message:
            print('Клиент отключился: ', client_address)
            break

        print(f'Сообщение от клиента {client_address}: {client_message}')

        server_response = input('Ответ сервера: ')
        if not server_response:
            server_response = 'Вы были отключены от сервера'
        client_socket.send(server_response.encode())

    client_socket.close()
