import random

# --- Utility Functions ---
def modinv(a, q):
    return pow(a, -1, q)

def text_to_nums(text):
    return [ord(c) for c in text]

def nums_to_text(nums):
    return "".join(chr(n) for n in nums)

# --- Key Generation ---
def elgamal_keygen(q, a):
    Xa = random.randint(2, q-2)  # private key
    Ya = pow(a, Xa, q)           # public key
    return (q, a, Ya), Xa

# --- Encryption ---
def elgamal_encrypt(pub_key, message):
    q, a, Ya = pub_key
    message_nums = text_to_nums(message)
    ciphertext = []

    print("\n--- ENCRYPTION DETAILS ---")
    for M in message_nums:
        b = random.randint(2, q-2)     # random key for encryption
        K = pow(Ya, b, q)              # shared secret key (sender side)
        c1 = pow(a, b, q)              # ciphertext part 1
        c2 = (M * K) % q               # ciphertext part 2


        ciphertext.append((c1, c2))

    return ciphertext

# --- Decryption ---
def elgamal_decrypt(Xa, q, ciphertext):
    recovered_nums = []

    print("\n--- DECRYPTION DETAILS ---")
    for c1, c2 in ciphertext:
        K = pow(c1, Xa, q)             # shared secret key (receiver side)
        M = (c2 * modinv(K, q)) % q

        recovered_nums.append(M)

    return nums_to_text(recovered_nums)

# --- MAIN ---
q = 467
a = 2

public_key, private_key = elgamal_keygen(q, a)

message = input("Enter message: ")
cipher = elgamal_encrypt(public_key, message)
plain_back = elgamal_decrypt(private_key, public_key[0], cipher)

print("\nPublic Key:", public_key)
print("Private Key:", private_key)
print("Encrypted:", cipher)
print("Decrypted:", plain_back)
