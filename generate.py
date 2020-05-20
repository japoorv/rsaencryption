from arithmetic import random_primes,gcd,inv
import random
import sys
def generate_keys():
    sys.setrecursionlimit(100000)
    p=random_primes()
    print ('Generated Prime1')
    q=random_primes()
    print ('Generated Prime2')
    while q==p:
        q=random_primes()
    while True:
        public_key=random.randint(1,(p-1)*(q-1))
        if (gcd(public_key,(p-1)*(q-1))==1):
            break
    print('Generated public_key')
    private_key=inv(public_key,(p-1)*(q-1))
    print('Generated public_key')
    file=open('config.py','a')
    file.write('\nprivate_key='+str(private_key)+'\n')
    file.write('public_key='+str(public_key)+'\n')
    file.write('n='+str(p*q)+'\n')
    file.write('symm_key='+str("'apoorvjain'"))
    file.close()
if __name__=='__main__':
    generate_keys()