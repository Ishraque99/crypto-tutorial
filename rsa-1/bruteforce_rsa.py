#!/usr/bin/python3

# sample script to bruteforce asymmetric cryptographic keys 
# that use small numbers.

from helpers import prime_factors

encrypted = [170, 80, 113, 86, 30, 95, 121, 4, 118, 130, 7, 167, 170, 80, 113, 86, 167, 59, 118, 130, 118, 97]
prod = 11*17
public_key = 3
encrypted_str = "".join(chr(n) for n in encrypted)
print(encrypted_str)

# need to figure out prime factors of prod
p, q = prime_factors(prod)
phi = (p-1)*(q-1)

# bruteforce a private key
priv = 1
while(((public_key*priv)%phi)!=1):
    priv = priv + 1

print(f"Found private: {priv}")
decrypted = [(n**priv)%prod for n in encrypted]
print("".join(chr(n) for n in decrypted))