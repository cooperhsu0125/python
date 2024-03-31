#########################匯入模組#########################
import socket

#########################函式與類別定義#########################

#########################宣告與設定#########################
HOST = "localhost"
PORT = 1228
sever_socket = socket.socket()
sever_socket.bind((HOST, PORT))
sever_socket.listen(5)
print("sever:{}port:{}start".format(HOST, PORT))
client, addr = sever_socket.accept()
print("client address:{},port:{}".format(addr[0], addr[1]))
#########################主程式#########################
while True:
    msg = client.recv(128).decode("utf8")
    print("Receive message:" + msg)
    reply = ""
    if msg == "Hi":
        reply = "Hello"
        client.send(reply.encode("utf8"))
    elif msg == "Bye":
        client.send(b"quit")
        break
    else:
        reply = "what?"
        client.send(reply.encode("utf8"))
    client.close()
    sever_socket.close()
#########################程式結束#########################
