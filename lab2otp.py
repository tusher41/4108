# --- OTP Encrypt / Decrypt with letter key ---
def otp_encrypt_letters(message, key):
    message = message.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    ciphertext = ""
    for i, ch in enumerate(message):  #enumerate diye index o character pawa jay
        c = (ord(ch) - 65 + ord(key[i]) - 65) % 26
        ciphertext += chr(c + 65)
    return ciphertext

def otp_decrypt_letters(ciphertext, key):
    key = key.upper().replace(" ", "")
    plaintext = ""
    for i, ch in enumerate(ciphertext):
        p = (ord(ch) - 65 - (ord(key[i]) - 65)) % 26
        plaintext += chr(p + 65)
    return plaintext

# --- MAIN ---
message = input("Enter your message: ")
key = input(f"Enter key (letters, same length as message): ")

cipher = otp_encrypt_letters(message, key)
print("Encrypted (A-Z letters):", cipher)

decrypted = otp_decrypt_letters(cipher, key)
print("Decrypted message:", decrypted)
