import socket

def main():
              host='127.0.0.1'
              port=5000
              s=socket.socket()
              s.bind((host,port))
              s.listen(1)
              c,addr=s.accept()
              print("Connection from:",addr)
              while True:
                            data=c.recv(1024)
                            if not data:
                                          break
                            print("From connected user",data)
                            data=data.upper()
                            print("Sending: ",data)
                            c.send(data.encode())
main()
