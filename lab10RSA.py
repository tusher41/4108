def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 3
    while gcd(e, phi) != 1:
        e += 2

    d = pow(e, -1, phi)   # built-in modular inverse
    return (e, n), (d, n)

def encrypt(pub, text):
    e, n = pub
    return [pow(ord(c), e, n) for c in text]

def decrypt(priv, cipher):
    d, n = priv
    return "".join(chr(pow(c, d, n)) for c in cipher)

# -------- MAIN --------
p = int(input("Enter p: "))
q = int(input("Enter q: "))

public_key, private_key = generate_keys(p, q)

print("Public Key:", public_key)
print("Private Key:", private_key)

message = input("Enter message: ")

cipher = encrypt(public_key, message)
print("Encrypted:", cipher)

plain = decrypt(private_key, cipher)
print("Decrypted:", plain)
