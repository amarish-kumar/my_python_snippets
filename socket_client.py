import socket

sock_client = socket.socket()
sock_client.connect(("localhost",9999))

while True:
    text = raw_input("> ")
    sock_client.send(text)
    if text == "quit":
        break    

print "bye!"
sock_client.close()