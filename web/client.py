import socket


def client_function(information):
    host = '127.0.0.1'
    port = 5001

    # création socket
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # envoi de la question
    mySocket.send(information.encode())

    # réception de la réponse
    data = mySocket.recv(1024).decode()
    print('Received from server: ' + data)

    # fermeture de la connexion
    mySocket.close()


msg = input("entre : ")
client_function(msg)

"""def client_function():
    print()
    host = '127.0.0.1'
    port = 5001

    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = input(" ? ")

    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()

        print('Received from server: ' + data)
        message = input(" ? ")

    mySocket.close()


client_function()
"""