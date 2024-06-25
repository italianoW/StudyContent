import random
import math

def is_prime(n):
  if n<2:
    return 0
  for temp in range(2,n//2+1):
    if n%temp==0:
      return 0
  return 1

def generate_prime(min,max):
  n = random.randint(min,max)
  while not is_prime(n):
    n = random.randint(min,max)
  return n

def generate_diff_prime(diff,min,max):
  n = generate_prime(min,max)
  while diff==n:
    n = generate_prime(min,max)
  return n

def inverse_module(e,mod_value):
  for d in range(3,mod_value):
    if (d * e) % mod_value == 1:
      return d
  raise ValueError("has no inverse")

def encrypt(m,e,n):
  message_encoded = [ord(ch) for ch in m]
  message_encrypted = [pow(ch,e,n) for ch in message_encoded]
  return message_encrypted

def decrypt(c,d,n):
  message_decrypted = [pow(ch,d,n) for ch in c]
  m = "".join(chr(ch) for ch in message_decrypted)
  return m

p = generate_prime(1000,2000)
q = generate_diff_prime(p,1000,2000)

print("p =",p," q =",q)

n = p*q
print("n =",n)

phi_n = (p-1)*(q-1)
print("phi =",phi_n)

e = generate_diff_prime(phi_n,10000,20000)
print("e =",e)
d = inverse_module(e,phi_n)
print("d =",d)

m = "Isso é uma senha especifica!"

print("\n","public key:",e,n)
c = encrypt(m,e,n)
print(c)

print("\n","private key:",d,n)
plaintext =  decrypt(c,d,n)
print(plaintext)
