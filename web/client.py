import socket


def client_function(information: str) -> dict:
    """
    Permet d'agir en tant que client et demander des informations à un serveur via un socket.

    PRE : 'information' est une string, et la valeur de la string dépend de l'information que l'on souhaite avoir
    POST : Retourne un dictionnaire contenant les informations demandées.
    """
    host = '127.0.0.1'
    port = 5001

    # création socket
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # envoi de la question
    mySocket.send(information.encode())

    # réception de la réponse sous forme de string --> on la transforme en dico
    data = mySocket.recv(1024).decode()
    data_dico = dict(eval(str(data)))
    # print('Received from server: ', data_dico)

    # fermeture de la connexion
    mySocket.close()

    return data_dico
