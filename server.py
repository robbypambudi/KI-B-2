# Author : Robby Ulung Pambudi
import socket

import DES

class Server:
  def __init__(self):
    self.key = '12345678'
    self.des = DES.DES(self.key)
    self.host = 'localhost'
    self.port = 12345
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
  def start(self):
    self.socket.bind((self.host, self.port))
    self.socket.listen(5)
    print('Server started')
    conn, addr = self.socket.accept()
    print('Connection from : ', addr)
    while True:
      data = conn.recv(1024).decode()
      if not data:
        break
      print('Received data : ', data)
      decrypted_data = self.des.decrypt(data)
      print('Decrypted data : ', decrypted_data)
      print("Enter Message to send to client")
      message = input()
      encrypted_message = self.des.encrypt(message)
      conn.send(encrypted_message.encode())
      
    conn.close()
    self.socket.close()
    
if __name__ == '__main__':
  server = Server()
  server.start()