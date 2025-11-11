def build_key_map(key_str):
    """Build substitution map from a 26-letter key string"""
    key_str = key_str.upper()
    if len(key_str) != 26 or len(set(key_str)) != 26:
        raise ValueError("Key must be 26 unique letters (A–Z).")
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return dict(zip(letters, key_str)) #zip() function diye letters o key_str er corresponding character gulo ke pair kora hoyeche

def encrypt(message, key_map):
    """Encrypt the message using the substitution key"""
    result = ""
    for char in message.upper():
        if char in key_map:
            result += key_map[char]
        else:
            result += char 
    return result

def decrypt(ciphertext, key_map):
    """Decrypt the ciphertext using the substitution key"""
    reverse_key = {v: k for k, v in key_map.items()}  
    result = ""
    for char in ciphertext:
        if char in reverse_key:
            result += reverse_key[char]
        else:
            result += char
    return result



message = input("Enter message: ")
key_input = input("Enter 26-letter key (unique letters A–Z): ")

try:
    key_map = build_key_map(key_input)

    encrypted = encrypt(message, key_map)
    print("Encrypted message:", encrypted)

    decrypted = decrypt(encrypted, key_map)
    print("Decrypted message:", decrypted)

except ValueError as e:
    print("Error:", e)
