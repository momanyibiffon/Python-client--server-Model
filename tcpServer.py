import socket

def Main():
    host = "127.0.0.1"
    port = 15200

    #new socket
    s = socket.socket()

    #binding new socket to a port
    s.bind((host,port))

    #listen for connections (1 connection at a time)
    s.listen(1)

    #accept fuction (c for connection, addr for address)
    c,addr = s.accept()

    print("Connection from" + str(addr))

    while True:
        data = c.recv(1024)
        if not data:
            break
        print("From connected user: "+str(data))
        data = str(data).upper()
        print("Sending: "+str(data))
        c.send(data.encode())

    c.close()

if __name__ == "__main__":
    Main()

     
    
