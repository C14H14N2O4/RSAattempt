import random
#    1. Choose two prime numbers p and q.
#    2. Compute n = p*q.
#    3. Calculate phi = (p-1) * (q-1).
#    4. Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1; i.e., e and phi(n) are coprime.
#    5. Calculate d as d ≡ e−1 (mod phi(n)); here, d is the modular multiplicative inverse of e modulo phi(n).
#    6. For encryption, c = me mod n, where m = original message.
#    7. For decryption, m = c d mod n.

# 816781324625613604021622328353
# 138111463853897940801393719267

def gcd(a: int, b: int) -> int:
    while b:
        a,b = b, a%b
    return a

def encrypt(p: int, q: int):
    n = p*q
    phi = (p-1) * (q-1)
    e = random.randint(1, (phi*n))
    while not 1 < e and not e < (phi*n) and not gcd(e, phi*n) ==1:
        e = random.randint(1, (phi*n))
    d = pow(e-1, -1, phi*n)
    secretNum = 9
    encrypted = pow(secretNum, e)
    print(encrypted)
    decrypted = pow(encrypted, d)
    decrypted = pow(decrypted, n)
    print(decrypted)


