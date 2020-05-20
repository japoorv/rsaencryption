from arithmetic import fast_exp 
from config import *
import sys
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import array
def encrypt(message,public_key,n): #storing message using symmetric cryptography and its key using assymetric
    key = get_random_bytes(16)
    cipher=AES.new(key,AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    file_out = open("encrypted.txt", "wb")
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    file_out.close()
    encrypted=[]
    for i in key:
        encrypted.append(str(fast_exp(i,public_key,n))+'\n')
    file_out=open('key.txt','w')
    file_out.writelines(encrypted)
    file_out.close()
    return
def decrypt(d,n):
    file_in=open('key.txt','r')
    key_=file_in.readlines()
    file_in.close()
    file_in=open('encrypted.txt','rb')
    key=[]
    for i in key_:
        key.append(fast_exp(int(i),d,n))
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    cipher_key=array.array('B',key).tobytes()
    cipher=AES.new(cipher_key,AES.MODE_EAX,nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data.decode('utf-8')
if __name__=='__main__':
    sys.setrecursionlimit(100000)
    choose=int(input("1 for encryption\n2 for decryption\n"))
    if choose==1:
        print ("Please type the text")
        message=input()
        encrypt(message,getPublicKey()[0],getPublicKey()[1])
    else :
        print (decrypt(getPrivateKey(),getPublicKey()[1]))