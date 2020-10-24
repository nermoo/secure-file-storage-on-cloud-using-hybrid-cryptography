from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import tkinter
import tkinter.filedialog
import tkinter
import hashlib




key=b'\x07\x12>\x1fH#V\xc4\x15\xf6\x84@z;\x87#\xe1\x0b,\xbb\xc0\xb8\xfc\xd6(,I\xd3|\x9c\x1a\xbc'

def pad(s):
    return s+ b'\0' * (AES.block_size- len(s)% AES.block_size)

def encrypt(message,key,key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv+cipher.encrypt(message)

def decrypt(ciphertext,key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")  #this is use for remove padding character

 

test=encrypt("hello",key)
print(test)
#use the code from first.py encryption methosds to padding otherwise all good to go problem is in the pad function
#implement the same functions from the first.py for encryption and decryption.