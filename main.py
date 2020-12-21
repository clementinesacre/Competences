import socket
import sys

#socket_family = AF_INET ou AF_UNIX
#socket_type = SOCK_STREAM ou SOCK_DGRAM
#s = socket.socket (socket_family, socket_type, protocol=0)
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # create an AF_INET, STREAM socket (TCP)
    sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err_msg:
    print('Unable to instantiate socket. Error code: ' + str(err_msg[0]) + ' , Error message : ' + err_msg[1])
    sys.exit()

sock_obj.connect(('http://services.groupkt.com/country/get/all', '80'))
kk = sock_obj.recv(2000)
print(kk)
sock_obj.close()




