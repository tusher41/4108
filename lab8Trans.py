# --- Encryption ---
def trans_encrypt(plaintext, key):
    plaintext = "".join(c.upper() for c in plaintext if c.isalpha())
    pad = 0
    if len(plaintext) % key != 0:
        pad = key - (len(plaintext) % key)
        plaintext += "X" * pad
    rows = [plaintext[i:i+key] for i in range(0, len(plaintext), key)]
    return "".join("".join(col) for col in zip(*rows)), pad

# --- Decryption ---
def trans_decrypt(ciphertext, key, pad):
    n_rows = len(ciphertext) // key
    cols = [ciphertext[i*n_rows:(i+1)*n_rows] for i in range(key)]
    plaintext = "".join("".join(row) for row in zip(*cols))
    if pad > 0:
        plaintext = plaintext[:-pad]  # remove ONLY added padding
    return plaintext

# --- MAIN ---
text = input("Enter plaintext: ")
k = int(input("Enter key (number of columns): "))

cipher, pad = trans_encrypt(text, k)
decipher = trans_decrypt(cipher, k, pad)

print("Encrypted:", cipher)
print("Decrypted:", decipher)