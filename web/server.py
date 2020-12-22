import socket
import time


def server_function():
    host = "127.0.0.1"
    port = 5001

    mySocket = socket.socket()
    mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mySocket.bind((host, port))

    # boucle pour écouter en permanence et ne pas s'arrêter
    new_data = ""
    while True:
        # écoute sur le port 5001
        mySocket.listen(1)

        # entend une demande, l'accepte
        conn, addr = mySocket.accept()

        # réception de la question
        data = conn.recv(1024).decode()
        if data == "coucou":
            new_data = "donnees"

        # envoie de la réponse
        conn.send(new_data.encode())

        # fermeture de la liaison
        conn.close()


server_function()

"""def server_function():
    host = "127.0.0.1"
    port = 5001

    mySocket = socket.socket()
    mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mySocket.bind((host, port))

    mySocket.listen(1)

    conn, addr = mySocket.accept()
    print("Connection from: " + str(addr))

    print("test clem")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected  user: " + str(data))

        data = str(data).upper()
        print("Received from User: " + str(data))

        data = input(" ? ")
        conn.send(data.encode())

    conn.close()


server_function()"""