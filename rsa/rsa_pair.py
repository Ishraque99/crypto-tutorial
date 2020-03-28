import random
from helpers import are_coprime

primes = [2, 3, 5, 7, 11, 13, 17]
p, q = random.sample(primes, 2)
print(f"p: {p}, q: {q}")
prod = p*q
phi = (p-1)*(q-1)
e = -1
for i in range(2, phi):
    if (are_coprime(i, prod) and
        are_coprime(i, phi)):
        e = i
        break
print(f"Public key: {e}")
priv = 1

while(((priv*e)%phi)!=1):
    priv += 1
print(f"Private key: {priv}")

plain = "hidden message!"
plain_num = [ord(c) for c in list(plain)]

# Encrypt
encrypted = []
for i in range(len(plain_num)):
    n = plain_num[i]
    encrypted.append((n**e)%prod)

# encrypted_str = "".join(chr(n) for n in encrypted)
print(encrypted)

# Decrypt
decrypted = []
for n in encrypted:
    d = (n**priv)%prod
    decrypted.append(d)

print(decrypted)
print("".join(chr(n) for n in decrypted))