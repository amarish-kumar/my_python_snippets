import socket

# server-side
sock_server = socket.socket()
sock_server.bind(("localhost",9999))
sock_server.listen(10)

sock_c, addr = sock_server.accept()
print "Client connected! From: ", addr

while True:
    text = sock_c.recv(1024)
    if text == "quit":
        break
    print "Recived:", text
    sock_c.send(text)

print "bye!"
sock_c.close()
sock_server.close()