import cv2, imutils, socket
# import numpy as np
# import time
import base64

BUFF_SIZE = 65536
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = 'localhost'#  socket.gethostbyname(host_name)
print(host_ip)
port = 9999
message = b'Hello'

client_socket.sendto(message,(host_ip,port))
fps,st,frames_to_count,cnt = (0,0,20,0)

vid = cv2.VideoCapture(0)
WIDTH=400
while True:
    
    # print("sending video")
    _,frame = vid.read()
    frame = imutils.resize(frame,width=WIDTH)
    encoded,buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
    message = base64.b64encode(buffer)
    client_socket.sendto(message,(host_ip,port))
    cv2.imshow('TRANSMITTING VIDEO FROM CLIENT -UDP',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
