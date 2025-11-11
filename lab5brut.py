def caesar_decrypt(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char
    return result


ciphertext = input("Enter encrypted message: ")

print("\nTrying all possible keys...\n")
for shift in range(26):  # 0–25 possible shifts
    decrypted = caesar_decrypt(ciphertext, shift)
    print(f"Key {shift:2d}: {decrypted}")
