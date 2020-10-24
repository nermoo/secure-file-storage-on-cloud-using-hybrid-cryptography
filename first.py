
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import tkinter
import tkinter.filedialog
import tkinter
import hashlib
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import tkinter as tk

def encrypt(info,key):
    msg=info
    BlOCK_SIZE=16
    PAD=b"%"
    padding=lambda s: s+ (BlOCK_SIZE-len(s) % BlOCK_SIZE) * PAD
    cipher=AES.new(new_pwd, AES.MODE_ECB)
    print(padding(msg))
    result=cipher.encrypt(padding(msg).encode('utf-8'))
    return result

def decrypt(info,key):
    msg=info
    PAD=b"%"
    decipher=AES.new(new_pwd,AES.MODE_ECB)
    pt=decipher.decrypt(msg).decode('utf-8')
    pad_index=pt.find(PAD)
    result=pt[:pad_index]
    return result

# password=input("enter password :")
# print(password)
# pwd=SHA256.new(password.encode('utf-8'))
# new_pwd=pwd.digest()
# print(new_pwd)
new_pwd=b'\x92\x94\xab8\x03\x9f`\xd2\xecS\x82/\xb4kR\xc6c\xaf~\xa4x\xf4\xd1{\xf4=\xa4N\xde^\x16l'


# msg="aravinda thma supirima"
# cipher_text=encrypt(msg)
# # print(cipher_text)
# print(cipher_text)


# plain_text=decrypt(cipher_text)
# print(plain_text)

filename= None

def encrypt_file(filename,new_pwd):
    with open(filename, 'rb') as f:
        plaintext=f.read()
    enc=encrypt(plaintext,new_pwd)
    with open(filename + ".enc", "wb") as f:
        f.write(enc)

def decrypt_file(filename,new_pwd):
    with open(filename, 'rb') as f:
        ciphertext=f.read()
    dec=decrypt(ciphertext, new_pwd)
    with open(filename[:-4], 'wb') as f:
         f.write(dec)

def load_text_file():
    global new_pwd,filename
    text_file= filedialog.askopenfile(filetypes=[('Text Files', '.txt')])
    if text_file.name != None:
        filename=text_file.name


def encrypt_the_file():
    global new_pwd,filename
    if filename != None:
        encrypt_file(filename, new_pwd)
    else:
        messagebox.showerror(title="error", message="There was no file loaded to encrypt")

def decrypt_the_file():
    global new_pwd, filename
    if filename!= None:
        fname=filename+ '.enc'
        decrypt_file(fname,new_pwd)
    else:
        messagebox.showerror(title="error", message="There was no file loaded to decrypt")



root=tkinter.Tk()
root.title('crypter')
root.minsize(width=200, height=200)
root.maxsize(width=300, height=300)


loadbutton=Button(root, text="load the text file", command=load_text_file)
encryptbutton=Button(root, text="Encrpyt", command=encrypt_the_file)
decryptbutton=Button(root, text="Decrypt", command=decrypt_the_file)


loadbutton.pack()
encryptbutton.pack()
decryptbutton.pack()

root.mainloop()