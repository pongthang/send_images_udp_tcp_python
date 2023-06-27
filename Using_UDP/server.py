import cv2, imutils, socket
import numpy as np
import time
import base64

BUFF_SIZE = 65536
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = '10.42.0.1'#  socket.gethostbyname(host_name)
print(host_ip)
port = 9999
socket_address = (host_ip,port)
server_socket.bind(socket_address)
print('Listening at:',socket_address)



msg,client_addr = server_socket.recvfrom(BUFF_SIZE)
print('GOT connection from ',client_addr)

print(msg)
while True:
    msg,client_addr = server_socket.recvfrom(BUFF_SIZE)

    #packet,_ = server_socket.recvfrom(BUFF_SIZE)
    data = base64.b64decode(msg,' /')
    npdata = np.frombuffer(data,dtype=np.uint8)
    frame = cv2.imdecode(npdata,1)

    cv2.imshow("RECEIVING VIDEO SERVER -UDP",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
# vid.release()
# # Destroy all the windows
cv2.destroyAllWindows()
    


