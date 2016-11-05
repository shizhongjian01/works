#coding:utf-8
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',8001))
sock.listen(5)
con,add=sock.accept()
while True:
	print("the server is %s"%add[0])
	word=input("server input>>>:")
	con.send(word.encode('gbk'))
	print(con.recv(2048).decode('utf-8'))
sock.close()
