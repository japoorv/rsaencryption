from arithmetic import fast_exp 
def encrypt(message,public_key,n): #only symmetric cryptography
    encrypted=[]
    for i in message:
        encrypted.append(fast_exp(i-'0',public_key,n))
    return encrypted
def decrypt(message,d,n):
    decrypted=[]
    for i in message:
        decrypted.append(fast_exp(i,d,n))
    return decrypted
