import socket
# import time
import cv2
import protocol.image_uav as img_pro


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8485))
connection = client_socket.makefile('wb')

cam = cv2.VideoCapture(0)

cam.set(3, 320);
cam.set(4, 240);

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:

    ret, frame_array = cam.read()
    result, frame = cv2.imencode('.jpg', frame_array, encode_param)
	
	#Meta data - put any data that should be sent along with images
    lat=10
    lon=10
    alt=10
    metadata={

            "lat":lat,
            'lon':lon,
            'alt':alt
        }


    client_socket.sendall(img_pro.send_msg(metadata,frame))

    cv2.imshow('Client Side !! Sending - TCP',frame_array)
    cv2.waitKey(1)

    # time.sleep(0.3) #delay
cam.release()
