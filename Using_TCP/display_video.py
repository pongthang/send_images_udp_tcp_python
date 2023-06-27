import socket
import cv2
import protocol.image_uav as img_pro



def socket_server(port):
    HOST=''
    PORT=port

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Socket created')

    s.bind((HOST,PORT))
    print('Socket bind complete')
    s.listen(10)
    print('Socket now listening')

    data = b""
    conn,addr=s.accept()
    while True:
        
        metadata,image,data = img_pro.get_msg(data,conn)

        # print(image.shape)
        frame = cv2.imdecode(image, cv2.IMREAD_COLOR)
        # print(frame.shape)
        print(metadata)
        

        cv2.imshow('Server Side -- receiving - TCP',frame)
        cv2.waitKey(1)


if __name__ == "__main__":
    port = 8485#int(input("Enter a port number: "))
    socket_server(port)
