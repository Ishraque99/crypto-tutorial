from helpers import prime_factors

encrypted = [91, 118, 100, 100, 62, 33, 98, 21, 62, 80, 80, 59, 38, 62, 110]
prod = 11*13
public_key = 7

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