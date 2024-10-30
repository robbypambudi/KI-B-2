from .decryption import decryption
from .encryption import encryption
from .helper import str_to_bin

class DES:
    def __init__(self, key):
        self.key = key
        

    def encrypt(self, plaintext):
        enc = encryption(plaintext)
        # Save the encrypted text to a file
        # with open('encrypted.txt', 'w', encoding='utf-8') as f:
        #     f.write(enc)
        return enc

    def decrypt(self, ciphertext):
        enc_to_binary = str_to_bin(ciphertext)
        return decryption(enc_to_binary)
