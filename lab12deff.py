# Diffie-Hellman Key Exchange (Simple Demo)

# Step 1: Public parameters
p = 23              # A prime number
g = 5               # A primitive root modulo p

# Step 2: Private keys (chosen secretly)
a = 6               # Alice's secret
b = 15              # Bob's secret

# Step 3: Generate public keys
A = pow(g, a, p)    # Alice computes g^a mod p
B = pow(g, b, p)    # Bob computes g^b mod p

# Step 4: Generate shared secret key
shared_key_alice = pow(B, a, p)   # (Bob's public key)^a mod p
shared_key_bob = pow(A, b, p)     # (Alice's public key)^b mod p

print("Alice's Public Key:", A)
print("Bob's Public Key:", B)
print("Shared Key (Alice):", shared_key_alice)
print("Shared Key (Bob):", shared_key_bob)
