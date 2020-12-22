from web import server, client
import socket
import sys

if __name__ == '__main__':


    # socket_family = AF_INET ou AF_UNIX
    # socket_type = SOCK_STREAM ou SOCK_DGRAM
    # s = socket.socket (socket_family, socket_type, protocol=0)
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """try:
        # create an AF_INET, STREAM socket (TCP)
        sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err_msg:
        print('Unable to instantiate socket. Error code: ' + str(err_msg[0]) + ' , Error message : ' + err_msg[1])
        sys.exit()

    sock_obj.connect(('www.google.com', 80))
    #sock_obj.sendall(b"GET / HTTP/1.1\r\n\r\n")
    sock_obj.sendall(b"GET / HTTP/1.1\r\nHost: www.google.com\r\nAccept: text/html\r\n\r\n")
    kk = sock_obj.recv(2000)
    print(kk)
    sock_obj.close()"""
    server.server_function()
    client.client_function()
    #client.client_function()



