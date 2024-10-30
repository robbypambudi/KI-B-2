import socket
import DES
class Client:
    def __init__(self, name):
        self.key = '12345678'
        self.des = DES.DES(self.key)
        self.port = 12345
        self.host = 'localhost'
    
    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        print('Connected to server')
        while True:
            print("Enter Message to send to server")
            message = input()
            encrypted_message = self.des.encrypt(message)
            self.socket.send(encrypted_message.encode())
            data = self.socket.recv(1024).decode()
            print('Received data : ', data)
            decrypted_data = self.des.decrypt(data)
            print('Decrypted data : ', decrypted_data)
            if message == 'exit':
                break
        self.socket.close()
        
if __name__ == '__main__':
    client = Client('client')
    client.start()
    