import socket
import time
import json
import pygame
ourwindow=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverconnect=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverconnect.bind(("127.0.0.1",9997))
serverconnect.listen(1)
client.connect(("127.0.0.1",9999))
client2,address2=serverconnect.accept()
while True:
    ourwindow.fill((0,0,0))
    try:
        data_to_send={"Hi":"Bye"}
        jsonstr=json.dumps(data_to_send)
        byte_data=jsonstr.encode('utf-8')
        client.sendall(byte_data)
    except:
        pass
    data=b""
    try:
        print("Client connected!")
        chunk=client2.recv(4096)#4 kb
        data+=chunk
        actualdatajson=data.decode("utf-8")
        actualdata=json.loads(actualdatajson)
        window=actualdata
    except:
        pass
    ourwindow.blit(window)
    pygame.display.update()